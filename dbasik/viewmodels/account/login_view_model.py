from starlette.requests import Request

from ..shared.viewmodel import ViewModelBase


class LoginViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.email: str = ""
        self.password: str = ""

    async def load(self):
        form = await self.request.form()
        self.email = form.get("email", "").lower().strip()
        self.password = form.get("password", "").strip()

        if not self.email or not self.email.strip():
            self.error = "You must specify an email."
        elif not self.password:
            self.error = "You must specify a password."
