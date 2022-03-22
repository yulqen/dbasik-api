import os
import os.path

from sqlalchemy.orm import Session

from web.data import db_session
from web.data.datamap import Datamap, DatamapLine
from web.data.project import Project, Tier, ProjectType, ProjectStage


def main():
    print("Initialising database.")
    init_db()
    print("Creating session.")
    session = db_session.create_session()
    print("Creating projects.")
    create_projects(session)
    print("Creating a datamap.")
    dm = create_datamap(session)
    create_datamap_lines(session, dm)


def create_datamap(session: Session) -> Datamap:
    session = db_session.create_session()
    tier = Tier(name="Tier 2", description="This is a test Tier 2")
    datamap = Datamap(name="Test Datamap", tier=tier)
    session.add(datamap)
    session.commit()
    session.close()
    return datamap


def create_datamap_lines(session: Session, datamap: Datamap) -> None:
    dmls = [
        DatamapLine(
            key=f"Test Key {tk}",
            datatype="TEXT",
            sheet="Test Sheet",
            cellref=f"A{tk}",
            datamap=datamap,
        )
        for tk in [str(x) for x in range(1, 99)]
    ]
    session.add_all(dmls)
    session.commit()
    session.close()


def create_projects(session: Session):
    session = db_session.create_session()
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
    session.close()


def init_db():
    top_dir = os.path.dirname(__file__)
    rel_file = os.path.join("db", "dbasik.sqlite")
    db_file = os.path.abspath(os.path.join(top_dir, rel_file))
    try:
        os.remove(db_file)
    except FileNotFoundError:
        pass
    print(f"Using {db_file}.")
    db_session.global_init(db_file)


if __name__ == "__main__":
    main()
