def test_index(client):
    response = client.get("/")
    assert response.url == "http://testserver/"
    assert response.status_code == 200


def test_projects_list_view(client, projects):
    response = client.get("/projects")
    assert "Boring Project" in response.text
    assert response.url == "http://testserver/projects"
