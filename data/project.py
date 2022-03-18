from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey, orm

from data.modelbase import SqlAlchemyBase


class Project(SqlAlchemyBase):
    __tablename__ = 'projects'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String)

    # Relationships
    project_type_name: str = Column(String, ForeignKey('project_types.name'))
    project_type = orm.relationship('ProjectType')
    project_stage_name: str = Column(String, ForeignKey('project_stages.name'))
    project_stage = orm.relationship('ProjectStage')
    tier_name: str = Column(String, ForeignKey('tiers.name'))
    tier = orm.relationship('Tier')


class ProjectType(SqlAlchemyBase):
    __tablename__ = 'project_types'

    name: str = Column(String, primary_key=True)
    description: str = Column(String)

    # Project relationship
    projects: List[Project] = orm.relation("Project", order_by=[
        Project.name.desc()
    ], back_populates='project_type')


class ProjectStage(SqlAlchemyBase):
    __tablename__ = 'project_stages'

    name: str = Column(String, primary_key=True)
    description: str = Column(String)

    # Project relationship
    projects: List[Project] = orm.relation("Project", order_by=[
        Project.name.desc()
    ], back_populates='project_stage')

    def __repr__(self):
        return f"<Project: {self.name}>"


class Tier(SqlAlchemyBase):
    __tablename__ = 'tiers'

    name: str = Column(String, primary_key=True)
    description: str = Column(String)

    # Project relationship
    projects: List[Project] = orm.relationship("Project", order_by=[
        Project.name.desc()
    ], back_populates='tier')
