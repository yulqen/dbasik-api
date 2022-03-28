import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from ..services.datamap_service import import_uploaded_csv_to_datamap
from ..exceptions import BadCSVError

from ..viewmodels.datamap.datamap_view_model import (
    DatamapListViewModel,
    DatamapDetailViewModel,
)

templates = Jinja2Templates(directory="web/templates")

router = fastapi.APIRouter()


@router.get("/datamaps")
def datamaps(request: Request):
    vm = DatamapListViewModel(request)
    return templates.TemplateResponse("datamaps/datamaps.html", vm.to_dict())


@router.get("/datamap/{id}")
def datamap(request: Request, id: int):
    vm = DatamapDetailViewModel(request, id)
    return templates.TemplateResponse("datamaps/datamap_detail.html", vm.to_dict())


@router.post("/datamaps")
def receive_datamap_csv(
    request: Request,
    dm_name: str = fastapi.Form(...),
    datamap_csv: fastapi.UploadFile = fastapi.File(...),
):
    try:
        import_uploaded_csv_to_datamap(datamap_csv, dm_name)
    except BadCSVError as e:
        vm = DatamapListViewModel(request)
        vm.error = e.args[0]
        return templates.TemplateResponse("datamaps/datamaps.html", vm.to_dict())
    return None
