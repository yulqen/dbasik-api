import csv
from fastapi import UploadFile
from dataclasses import dataclass
from pathlib import Path
from typing import List
from codecs import iterdecode

from ..data import db_session
from ..exceptions import BadCSVError
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
    """Handles a CSV file passed from the file system and inserts lines into database."""
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
    """Handles a CSV file uploaded by a form, as a fastapi.UploadFile()."""
    dmls = []
    if not f.filename.endswith("csv"):
        raise BadCSVError("Not a valid CSV file.")
    csvfile = csv.DictReader(iterdecode(f.file, "utf-8"))
    keys = set(csvfile.fieldnames)
    kopts = set(["KEY", "Key", "key"]) & keys
    sopts = set(["Sheet", "sheet"]) & keys
    dtypeopts = set(["type", "datatype"]) & keys
    cropts = set(["type", "cellref"]) & keys
    if not all([kopts, sopts, dtypeopts, cropts]):
        if not kopts:
            raise BadCSVError("key header is not correct.")
        elif not sopts:
            raise BadCSVError("sheet header is not correct.")
        elif not dtypeopts:
            raise BadCSVError("datatype header is not correct.")
        else:
            raise BadCSVError("cellref header is not correct.")
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


def check_csv(f: UploadFile) -> bool:
    """Checks CSV for correct headers. Raises exceptions where necessary."""
    csvfile = csv.DictReader(iterdecode(f.file, "utf-8"))
    keys = set(csvfile.fieldnames)
    kopts = set(["KEY", "Key", "key"]) & keys
    sopts = set(["Sheet", "sheet"]) & keys
    dtypeopts = set(["type", "datatype"]) & keys
    cropts = set(["type", "cellref"]) & keys
    if not all([kopts, sopts, dtypeopts, cropts]):
        if not kopts:
            raise BadCSVError("key header is not correct.")
        elif not sopts:
            raise BadCSVError("sheet header is not correct.")
        elif not dtypeopts:
            raise BadCSVError("datatype header is not correct.")
        else:
            raise BadCSVError("cellref header is not correct.")
    return True
