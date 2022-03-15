import fastapi
from starlette import status
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from infrastructure import cookie_auth
from services import user_service
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


@router.post("/account/register")
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()
    if vm.error:
        return templates.TemplateResponse("account/register.html", vm.to_dict())
    # Create the account
    account = user_service.create_account(vm.name, vm.email, vm.password)

    # Log in user
    response = fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)
    return response


@router.get("/account/login")
def login(request: Request):
    vm = LoginViewModel(request)
    return templates.TemplateResponse("account/login.html", vm.to_dict())


@router.get("/account/logout")
def logout():
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)
    return response
