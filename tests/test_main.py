import pytest
from web.data.datamap import Datamap
from web.services.datamap_service import (
    get_datamap_lines,
    get_datamaps,
    import_csv_to_datamap,
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


def test_import_csv_lines_to_datamap(dm_csv, datamap, session):
    import_csv_to_datamap(dm_csv, datamap)
    session = session()
    dm = session.query(Datamap).first()
    assert dm.lines[0].key == "Test Key 1"


def test_datamapline_from_conftest(datamapline):
    assert datamapline.key == "Test Key 1"
    assert datamapline.sheet == "Test Sheet"
    assert datamapline.cellref == "A10"
    assert datamapline.datamap.name == "Test Datamap"
    assert datamapline.datamap.tier.name == "Tier 2"
