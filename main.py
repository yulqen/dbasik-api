from pathlib import Path

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from data import db_session
from views import account
from views import datamap
from views import home
from views import project

app = FastAPI(title="dbasik - datamaps for the web",
              description='Stop using spreadsheets to store data. Extract with dbasik.',
              version='1.0')


def configure():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(project.router)
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(datamap.router)
    config_db()


def config_db():
    file = (Path(__file__).parent / 'db' / 'dbasik.sqlite').absolute()
    db_session.global_init(file.as_posix())


def main():
    configure()
    uvicorn.run(app)


if __name__ == "__main__":
    main()
