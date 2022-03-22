import os
from pathlib import Path

import pytest
from server import app
from populate import create_projects, create_datamap, create_datamap_lines
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
    create_projects(session)


@pytest.fixture
def datamap(session):
    datamap = create_datamap(session)
    yield datamap


@pytest.fixture
def datamaplines(datamap, session):
    session = session()
    create_datamap_lines(session, datamap)


@pytest.fixture
def dm_csv():
    f = Path.cwd() / "tests" / "resources" / "dm_csv.csv"
    return f
