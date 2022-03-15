import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from viewmodels.account.account_view_model import AccountViewModel
from viewmodels.account.login_view_model import LoginViewModel
from viewmodels.account.register_view_model import RegisterViewModel

router = fastapi.APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/account")
def account(request: Request):
    vm = AccountViewModel(request)
    return templates.TemplateResponse("account/index.html", vm.to_dict())


@router.get("/account/register")
def register(request: Request):
    vm = RegisterViewModel(request)
    return templates.TemplateResponse("account/register.html", vm.to_dict())


@router.get("/account/login")
def login(request: Request):
    vm = LoginViewModel(request)
    return templates.TemplateResponse("account/login.html", vm.to_dict())


@router.get("/account/logout")
def logout():
    return {}
