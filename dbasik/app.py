from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from .views import account, datamap, home, project

app = FastAPI(title="dbasik - datamaps for the web", version="1.0.0")

app.mount("/static", StaticFiles(directory="dbasik/static"), name="static")
app.include_router(project.router)
app.include_router(home.router)
app.include_router(account.router)
app.include_router(datamap.router)
