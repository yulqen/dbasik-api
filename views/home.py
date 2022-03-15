import fastapi
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from viewmodels.home.index_view_model import IndexViewModel
from viewmodels.shared.viewmodel import ViewModelBase

templates = Jinja2Templates(directory="templates")

router = fastapi.APIRouter()


@router.get("/")
async def index(request: Request):
    vm = IndexViewModel(request, 3)
    return templates.TemplateResponse("home/index.html", vm.to_dict())


@router.get("/about")
def about(request: Request):
    vm = ViewModelBase(request)
    return templates.TemplateResponse("home/about.html", vm.to_dict())
