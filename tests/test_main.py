import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from server import app
from web.data.modelbase import SqlAlchemyBase
from web.data.project import Project, ProjectStage, ProjectType, Tier
from web.views import home

app.include_router(home.router)


SQLALCHEMY_DB_URL = "sqlite:///test.db"
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SqlAlchemyBase.metadata.create_all(bind=engine)

client = TestClient(app)

@pytest.fixture
def projects():
    session = TestingSessionLocal()
    project_type = ProjectType(name="Boring Project", description="Bollocks")
    project_stage = ProjectStage(name="Stage 1", description="Russles")
    tier = Tier(name="Tier 1", description="This is a test Tier")
    session.add_all([project_stage, project_type, tier])
    session.commit()

    ps = []
    for p in ["AAA", "AAB", "ABB", "BBB", "BOOB"]:
        ps.append(
            Project(
                name=f"Test Project {p}",
                project_stage=project_stage,
                project_type=project_type,
                tier=tier,
            )
        )
    session.add_all(ps)
    session.commit()
    yield
    os.remove("test.db")

def test_index():
    project_type = ProjectType(name="Boring Project", description="Bollocks")
    project_stage = ProjectStage(name="Stage 1", description="Russles")
    tier = Tier(name="Tier 1", description="This is a test Tier")
    project = Project(
        name=f"Test Project",
        project_stage=project_stage,
        project_type=project_type,
        tier=tier,
    )
    session = TestingSessionLocal()
    session.add_all([project_stage, project_type, tier, project])
    session.commit()
    response = client.get("/")
    assert response.url == 'http://testserver/'
    assert response.status_code == 200


def test_projects_list_view(projects, monkeypatch):
    monkeypatch.setattr("web.data.db_session.__factory", TestingSessionLocal, raising=True)
    response = client.get("/projects")
    assert "Boring Project" in response.text
    assert response.url == 'http://testserver/projects'

