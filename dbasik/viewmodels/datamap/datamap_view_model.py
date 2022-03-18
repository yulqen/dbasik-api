from starlette.requests import Request

from ...services import datamap_service
from ..shared.viewmodel import ViewModelBase


class DatamapListViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.datamaps = datamap_service.get_datamaps()

        if not self.datamaps:
            return
