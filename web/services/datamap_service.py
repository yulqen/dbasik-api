from typing import List, Optional

from ..data import db_session
from ..data.datamap import Datamap, DatamapLine


def get_datamaps() -> Optional[List[Datamap]]:
    session = db_session.create_session()
    return session.query(Datamap).all()


def get_datamap_lines() -> Optional[List[DatamapLine]]:
    pass
