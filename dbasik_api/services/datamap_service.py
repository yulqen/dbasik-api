from typing import Optional, List

from dbasik_api.data import db_session
from dbasik_api.data.datamap import Datamap


def get_datamaps() -> Optional[List[Datamap]]:
    session = db_session.create_session()
    return session.query(Datamap).all()
