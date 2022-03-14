from typing import Optional, List

from data.project import Project


def get_project_by_id(project_id) -> Optional[Project]:
    return Project("Another test project", project_id, "Boring Project", "15m")


def get_budget_by_id(project_id: int):
    return Project("Another test project", project_id, "Boring Project", "15m")


def get_type_by_id(project_id: int):
    return Project("Another test project", project_id, "Boring Project", "15m")


def get_name_by_id(project_id: int):
    return Project("Another test project", project_id, "Boring Project", "15m")


def major_projects(limit: int = 2) -> list[dict[str, str | int]]:
    return [
               {
                   "budget": "20M",
                   "type": "Rubbish",
                   "name": "Railway Reclaimation Project",
                   "id": 1,
               },
               {"budget": "40M", "type": "Useless", "name": "Stanley Banks Head Scheme", "id": 2},
               {
                   "budget": "50M",
                   "type": "Trumpets",
                   "name": "Rocking Robots Closure Meak",
                   "id": 3,
               },
               {"budget": "200M", "type": "Rollocks", "name": "Bomba Clifton Hedges", "id": 4},
           ][:limit]


def project_count() -> int:
    return 20


def get_projects() -> Optional[List[Project]]:
    return [
        Project("Another test project 1", 1, "Boring Project", "15m"),
        Project("Another test project 2", 2, "Boring Project", "15m"),
        Project("Another test project 3", 3, "Boring Project", "15m"),
        Project("Another test project 4", 4, "Boring Project", "15m"),
    ]
