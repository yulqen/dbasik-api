import fastapi
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

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
    return templates.TemplateResponse(
        "projects/projects.html", {"request": request, "projects": dummy_projects}
    )


@router.get("/projects/{project_id}")
def get_project(request: Request, project_id: int):
    p = [pj for pj in dummy_projects if project_id == pj["id"]]
    p = p[0]
    return templates.TemplateResponse(
        "projects/project.html",
        {"request": request, "project_id": project_id, "project": p},
    )
