from sqlalchemy import Column, Integer, String, ForeignKey, orm

from data.modelbase import SqlAlchemyBase
from data.project import Tier


class Datamap(SqlAlchemyBase):
    __tablename__ = 'datamaps'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String)

    # Relationships
    tier_name: Tier = Column(String, ForeignKey('tiers.name'))
    tier = orm.relationship('Tier')
