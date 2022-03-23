from starlette.requests import Request

from ...services import datamap_service
from ..shared.viewmodel import ViewModelBase


class DatamapListViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.datamaps = datamap_service.get_datamaps()

        if not self.datamaps:
            return


class DatamapDetailViewModel(ViewModelBase):
    def __init__(self, request: Request, id: int):
        super().__init__(request)
        self.datamap = datamap_service.get_datamap_by_id(id)

        if not self.datamap:
            return

        self.datamap_lines = datamap_service.get_datamap_lines_for_datamap(self.datamap)
