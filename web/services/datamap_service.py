import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from ..data import db_session
from ..data.datamap import Datamap, DatamapLine


@dataclass
class DML:
    key: str
    datatype: str
    sheet: str
    cellref: str


def get_datamaps() -> Optional[List[Datamap]]:
    session = db_session.create_session()
    return session.query(Datamap).all()


def get_datamap_lines() -> Optional[List[DatamapLine]]:
    pass


def import_csv_to_datamap(csvf: Path, datamap: Datamap) -> None:
    dmls = []
    with open(csvf, "r", encoding="utf-8") as f:
        csvfile = csv.DictReader(f)
        for row in csvfile:
            dmls.append(DML(**row))
    session = db_session.create_session()
    for d in dmls:
        _d = DatamapLine(
            key=d.key,
            datatype=d.datatype,
            sheet=d.sheet,
            cellref=d.cellref,
            datamap=datamap,
        )
        session.add(_d)
    session.commit()
    session.close()
