import os

import pytest
from server import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient
from web.data.datamap import Datamap, DatamapLine
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


@pytest.fixture
def datamap(session):
    session = session()
    tier = Tier(name="Tier 2", description="This is a test Tier 2")
    datamap = Datamap(name="Test Datamap", tier=tier)
    session.add(datamap)
    session.commit()
    yield datamap


@pytest.fixture
def datamapline(datamap, session):
    session = session()
    dm = session.query(Datamap).first()
    dml = DatamapLine(
        key="Test Key 1", datatype="TEXT", sheet="Test Sheet", cellref="A10", datamap=dm
    )
    session.add(dml)
    session.commit()
    yield dml
