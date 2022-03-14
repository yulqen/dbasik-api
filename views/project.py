import fastapi
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from viewmodels.project.project_view_model import ProjectDetailViewModel, ProjectListViewModel

templates = Jinja2Templates(directory="templates")

router = fastapi.APIRouter()

dummy_projects = [
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
]


@router.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    vm = ProjectListViewModel(request)
    return templates.TemplateResponse(
        "projects/projects.html", vm.to_dict()
    )


@router.get("/projects/{project_id}")
def project_detail(request: Request, project_id: int):
    vm = ProjectDetailViewModel(project_id, request)
    return templates.TemplateResponse(
        "projects/project_detail.html",
        vm.to_dict()
    )
