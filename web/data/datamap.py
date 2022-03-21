from typing import List

from sqlalchemy import Column, ForeignKey, Integer, String, orm

from ..data.modelbase import SqlAlchemyBase
from ..data.project import Tier


class DatamapLine(SqlAlchemyBase):
    __tablename__ = "datamap_lines"

    id: int = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    key: str = Column(String)  # type: ignore
    datatype: str = Column(String)  # type: ignore
    sheet: str = Column(String)  # type: ignore
    cellref: str = Column(String)  # type: ignore

    # Relationships
    datamap_id: "Datamap" = Column(Integer, ForeignKey("datamaps.id"))  # type: ignore
    datamap = orm.relationship("Datamap")  # type: ignore


class Datamap(SqlAlchemyBase):
    __tablename__ = "datamaps"

    id: int = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    name: str = Column(String)  # type: ignore

    # Relationships
    tier_name: Tier = Column(String, ForeignKey("tiers.name"))  # type: ignore
    tier = orm.relationship("Tier")
    lines: List[DatamapLine] = orm.relationship(
        "DatamapLine", order_by=[DatamapLine.id], back_populates="datamap"
    )
