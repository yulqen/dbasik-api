from fastapi import FastAPI
import uvicorn

from views import project
from views import home
from views import account
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(project.router)
app.include_router(home.router)
app.include_router(account.router)

if __name__ == "__main__":
    uvicorn.run(app)
