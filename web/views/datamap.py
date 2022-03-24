import csv
import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

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
    dm_name: str = fastapi.Form(...),
    datamap_csv: fastapi.UploadFile = fastapi.File(...),
):
    breakpoint()
    lines = csv.reader(datamap_csv.file)
    for l in lines:
        print(l)
    return None
