from pathlib import Path

import uvicorn

from dbasik.data import db_session
from dbasik.app import app


def config_db():
    file = (Path(__file__).parent / "db" / "dbasik.sqlite").absolute()
    db_session.global_init(file.as_posix())


def main():
    config_db()
    uvicorn.run(app)


if __name__ == "__main__":
    main()
