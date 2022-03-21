
def test_index(client):
    response = client.get("/")
    assert response.url == 'http://testserver/'
    assert response.status_code == 200


def test_projects_list_view(session, client, projects, monkeypatch):
    monkeypatch.setattr("web.data.db_session.__factory", session, raising=True)
    response = client.get("/projects")
    assert "Boring Project" in response.text
    assert "Test Project" in response.text
    assert response.url == 'http://testserver/projects'

