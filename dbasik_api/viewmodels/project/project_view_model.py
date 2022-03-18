from starlette.requests import Request

from dbasik_api.services import project_service
from dbasik_api.viewmodels.shared.viewmodel import ViewModelBase


class ProjectDetailViewModel(ViewModelBase):
    def __init__(self, project_id: int, request: Request):
        super().__init__(request)
        self.type = project_service.get_type_by_id(project_id)
        self.name = project_service.get_name_by_id(project_id)
        self.budget = project_service.get_budget_by_id(project_id)
        self.project = project_service.get_project_by_id(project_id)

        if not self.project:
            return


class ProjectListViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.projects = project_service.get_projects()

        if not self.projects:
            return
