from typing import List

from starlette.requests import Request

from ...services import project_service, user_service
from ...viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request, project_limit: int):
        super().__init__(request)

        self.project_count: int = project_service.project_count()
        # self.major_projects: List = project_service.major_projects(limit=project_limit)
        self.user_count: int = user_service.user_count()
