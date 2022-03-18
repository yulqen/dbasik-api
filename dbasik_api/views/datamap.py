import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from dbasik_api.viewmodels.datamap.datamap_view_model import DatamapListViewModel

templates = Jinja2Templates(directory="templates")

router = fastapi.APIRouter()


@router.get("/datamaps")
def datamaps(request: Request):
    vm = DatamapListViewModel(request)
    return templates.TemplateResponse(
        "datamaps/datamaps.html", vm.to_dict()
    )
