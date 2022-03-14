import fastapi
from starlette.requests import Request

from viewmodels.account.account_view_model import AccountViewModel
from viewmodels.account.login_view_model import LoginViewModel
from viewmodels.account.register_view_model import RegisterViewModel

router = fastapi.APIRouter()


@router.get("/account")
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get("/account/register")
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.get("/account/login")
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get("/account/logout")
def logout():
    return {}
