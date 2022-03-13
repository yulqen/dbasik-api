import fastapi
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = fastapi.APIRouter()


@router.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse("projects/projects.html", {"request": request})


@router.get("/project/{project_id}")
def get_project(request: Request, project_id: int):
    return templates.TemplateResponse(
        "projects/project.html", {"request": request, "project_id": project_id}
    )
