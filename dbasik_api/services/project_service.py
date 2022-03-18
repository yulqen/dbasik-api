from typing import Optional, List

from dbasik_api.data import db_session
from dbasik_api.data.project import Project


def get_project_by_id(project_id) -> Optional[Project]:
    return Project("Another test project", project_id, "Boring Project", "15m")


def get_budget_by_id(project_id: int):
    return Project("Another test project", project_id, "Boring Project", "15m")


def get_type_by_id(project_id: int):
    return Project("Another test project", project_id, "Boring Project", "15m")


def get_name_by_id(project_id: int):
    return Project("Another test project", project_id, "Boring Project", "15m")


def major_projects(limit: int = 2) -> list[dict[str, str | int]]:
    session = db_session.create_session()
    return session.query(Project).all()[:limit]


def project_count() -> int:
    return 12


def get_projects() -> Optional[List[Project]]:
    session = db_session.create_session()
    projects = session.query(Project).all()
    return projects
