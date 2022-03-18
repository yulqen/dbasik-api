import os.path

from data import db_session
from data.datamap import Datamap
from data.project import Project, Tier, ProjectType, ProjectStage


def main():
    init_db()
    create_projects()
    create_datamaps()


def create_datamaps():
    session = db_session.create_session()
    tier = Tier(name="Tier 2", description="This is a test Tier 2")
    datamap = Datamap(name='Test Datamap', tier=tier)
    session.add(datamap)
    session.commit()


def create_projects():
    session = db_session.create_session()
    project_type = ProjectType(name="Boring Project", description="Bollocks")
    project_stage = ProjectStage(name="Stage 1", description="Russles")
    tier = Tier(name="Tier 1", description="This is a test Tier")
    session.add_all([project_stage, project_type, tier])
    session.commit()

    ps = []
    for p in ['AAA', 'AAB', 'ABB', 'BBB', 'BOOB']:
        ps.append(Project(name=f"Test Project {p}", project_stage=project_stage,
                          project_type=project_type,
                          tier=tier))
    session.add_all(ps)
    session.commit()


def init_db():
    top_dir = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'dbasik.sqlite')
    db_file = os.path.abspath(os.path.join(top_dir, rel_file))
    try:
        os.remove(db_file)
    except Exception as e:
        pass
    print(f"Using {db_file}.")
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()
