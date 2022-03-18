from typing import Optional, List

from data import db_session
from data.datamap import Datamap


def get_datamaps() -> Optional[List[Datamap]]:
    session = db_session.create_session()
    return session.query(Datamap).all()
