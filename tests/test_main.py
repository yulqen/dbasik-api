from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from web.data.project import ProjectType, ProjectStage, Project, Tier

from web.views import home
from web.data.modelbase import SqlAlchemyBase
from server import app

app.include_router(home.router)


SQLALCHEMY_DB_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SqlAlchemyBase.metadata.create_all(bind=engine)

client = TestClient(app)


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
    assert response.status_code == 200
