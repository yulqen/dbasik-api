import fastapi
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from ..viewmodels.project.project_view_model import (
    ProjectDetailViewModel,
    ProjectListViewModel,
)

templates = Jinja2Templates(directory="dbasik/templates")

router = fastapi.APIRouter()


@router.get("/projects")
def projects(request: Request):
    vm = ProjectListViewModel(request)
    return templates.TemplateResponse("projects/projects.html", vm.to_dict())


@router.get("/projects/{project_id}")
def project_detail(request: Request, project_id: int):
    vm = ProjectDetailViewModel(project_id, request)
    return templates.TemplateResponse("projects/project_detail.html", vm.to_dict())
