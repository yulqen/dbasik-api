from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey, orm

from .modelbase import SqlAlchemyBase

class Project(SqlAlchemyBase):
    __tablename__ = "projects"

    id: int = Column(Integer, primary_key=True, autoincrement=True)  #type: ignore
    name: str = Column(String) #type: ignore

    # Relationships
    project_type_name: str = Column(String, ForeignKey("project_types.name"))  #type: ignore
    project_type = orm.relationship("ProjectType")  #type: ignore
    project_stage_name: str = Column(String, ForeignKey("project_stages.name"))  #type: ignore
    project_stage = orm.relationship("ProjectStage")
    tier_name: str = Column(String, ForeignKey("tiers.name")) #type: ignore
    tier = orm.relationship("Tier")


class ProjectType(SqlAlchemyBase):
    __tablename__ = "project_types"

    name: str = Column(String, primary_key=True)  #type: ignore
    description: str = Column(String) #type: ignore

    # Project relationship
    projects: List[Project] = orm.relation(
        "Project", order_by=[Project.name.desc()], back_populates="project_type"
    )  #type: ignore


class ProjectStage(SqlAlchemyBase):
    __tablename__ = "project_stages"

    name: str = Column(String, primary_key=True)   #type: ignore
    description: str = Column(String)   #type: ignore

    # Project relationship
    projects: List[Project] = orm.relation(
        "Project", order_by=[Project.name.desc()], back_populates="project_stage"
    )

    def __repr__(self):
        return f"<Project: {self.name}>"


class Tier(SqlAlchemyBase):
    __tablename__ = "tiers"

    name: str = Column(String, primary_key=True)   #type: ignore
    description: str = Column(String)   #type: ignore

    # Project relationship
    projects: List[Project] = orm.relationship(
        "Project", order_by=[Project.name.desc()], back_populates="tier"
    )   #type: ignore
