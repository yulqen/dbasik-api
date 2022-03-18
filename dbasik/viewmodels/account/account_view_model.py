from starlette.requests import Request

from dbasik.services import user_service
from dbasik.viewmodels.shared.viewmodel import ViewModelBase


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user = user_service.get_user_by_id(self.user_id)
