from pathlib import Path
from typing import Callable, Optional

import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from .modelbase import SqlAlchemyBase

__factory: Optional[Callable[[], Session]] = None


def global_init(db_file: str):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a database file.")

    folder = Path(db_file).parent
    folder.mkdir(parents=True, exist_ok=True)

    conn_str = "sqlite:///" + db_file.strip()
    print("Connecting to DB with {}".format(conn_str))

    engine = sqlalchemy.create_engine(
        conn_str, echo=False, connect_args={"check_same_thread": False}
    )
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import web.data.__all_models  # this import 'sees' our 'model' classes in data...

    SqlAlchemyBase.metadata.create_all(
        engine
    )  # ...so that SqlAlchemy can create the tables here


def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception("You must call global_init() before using this method.")

    session: Session = __factory()
    session.expire_on_commit = False
    return session
