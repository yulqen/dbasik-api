from web.data.datamap import Datamap
from web.services.datamap_service import get_datamaps


def test_index(client):
    response = client.get("/")
    assert response.url == "http://testserver/"
    assert response.status_code == 200


def test_projects_list_view(client, projects):
    response = client.get("/projects")
    assert "Boring Project" in response.text
    assert response.url == "http://testserver/projects"


def test_datamap_in_db(session, datamaps):
    session = session()
    dm = session.query(Datamap).first()
    # TODO: this doesn't test our API
    assert dm.name == "Test Datamap"


def test_datamap_service(datamaps):
    dms = get_datamaps()
    assert dms[0].name == "Test Datamap"  # type: ignore
