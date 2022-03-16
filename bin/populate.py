import os.path

from data import db_session
from data.user import User


def main():
    init_db()
    session = db_session.create_session()
    user = User()
    user.name = "Toggo"
    user.email = "toggo@example.com"
    session.add(user)
    session.commit()


def init_db():
    top_dir = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'dbasik.sqlite')
    db_file = os.path.abspath(os.path.join(top_dir, rel_file))
    print(f"Using {db_file}.")
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()
