import csv
from fastapi import UploadFile
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
from codecs import iterdecode

from ..data import db_session
from ..data.datamap import Datamap, DatamapLine


@dataclass
class DML:
    key: str
    datatype: str
    sheet: str
    cellref: str


def get_datamaps() -> List[Datamap] | None:
    session = db_session.create_session()
    return session.query(Datamap).all()


def get_datamap_by_id(id: int) -> Datamap | None:
    session = db_session.create_session()
    return session.query(Datamap).filter_by(id=id).one()


def get_datamap_lines_for_datamap(datamap: Datamap) -> List[DatamapLine] | None:
    session = db_session.create_session()
    dmls = session.query(DatamapLine).filter_by(datamap_id=datamap.id).all()
    return dmls


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


def import_uploaded_csv_to_datamap(f: UploadFile, datamap: str) -> None:
    dmls = []
    csvfile = csv.DictReader(iterdecode(f.file, "utf-8"))
    for row in csvfile:
        dmls.append(DML(**row))
    session = db_session.create_session()
    dm = Datamap(name=datamap)
    for d in dmls:
        _d = DatamapLine(
            key=d.key,
            datatype=d.datatype,
            sheet=d.sheet,
            cellref=d.cellref,
            datamap=dm,
        )
        session.add(_d)
    session.commit()
    session.close()
