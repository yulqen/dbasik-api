import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from starlette.testclient import TestClient

from server import app
from web.data.modelbase import SqlAlchemyBase
from web.data.project import Project, ProjectStage, ProjectType, Tier
from web.views import home


@pytest.fixture
def session(monkeypatch):
    SQLALCHEMY_DB_URL = "sqlite:///test.db"
    engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine, expire_on_commit=False
    )
    monkeypatch.setattr(
        "web.data.db_session.__factory", TestingSessionLocal, raising=True
    )
    SqlAlchemyBase.metadata.create_all(bind=engine)
    yield TestingSessionLocal
    os.remove("test.db")


@pytest.fixture
def client():
    app.include_router(home.router)
    yield TestClient(app)


@pytest.fixture
def projects(session):
    project_type = ProjectType(name="Boring Project", description="Bollocks")
    project_stage = ProjectStage(name="Stage 1", description="Russles")
    tier = Tier(name="Tier 1", description="This is a test Tier")
    session = session()
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
    session.close()
