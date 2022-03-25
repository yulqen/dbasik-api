from fastapi.datastructures import UploadFile
from web.data.datamap import Datamap, DatamapLine
from web.services.datamap_service import (
    get_datamaps,
    import_csv_to_datamap,
    get_datamap_by_id,
    get_datamap_lines_for_datamap,
    import_uploaded_csv_to_datamap,
)


def test_index(client):
    response = client.get("/")
    assert response.url == "http://testserver/"
    assert response.status_code == 200


def test_projects_list_view(client, projects):
    response = client.get("/projects")
    assert "Boring Project" in response.text
    assert response.url == "http://testserver/projects"


def test_datamap_in_db(session, datamap):
    session = session()
    dm = session.query(Datamap).first()
    # TODO: this doesn't test our API
    assert dm.name == "Test Datamap"


def test_datamap_service(datamap):
    dms = get_datamaps()
    assert dms[0].name == "Test Datamap"  # type: ignore


def test_get_datamap_by_id(datamap):
    assert get_datamap_by_id(1).name == "Test Datamap"  # type: ignore


def test_get_datamap_lines_for_datamap(datamap, datamaplines):
    dmls = get_datamap_lines_for_datamap(datamap)
    assert dmls[0].datamap.id == datamap.id


def test_import_csv_lines_to_datamap(dm_csv, datamaplines, datamap, session):
    import_csv_to_datamap(dm_csv, datamap)
    session = session()
    dm = session.query(Datamap).first()
    assert dm.lines[-1].key == "Test Key from CSV 2"


def test_import_upload_datmap_csv(dm_csv, datamaplines, datamap, session):
    f = open(dm_csv, "rb")
    uf = UploadFile("toss.csv", f, "text/csv")
    import_uploaded_csv_to_datamap(uf, datamap.name)
    session = session()
    dml = session.query(DatamapLine).first()
    assert dml.key == "Test Key 1"
