from fastapi import FastAPI

from views import project
from views import home
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(project.router)
app.include_router(home.router)


@app.get("/")
async def index():
    return {"message": "Hello index page"}
