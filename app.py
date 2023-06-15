from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.api.endpoints import router as api_router
from src.main.views import router as main_router


app = FastAPI()
app.include_router(router=api_router)
app.include_router(router=main_router)
app.mount(
    path='/static',
    app=StaticFiles(directory='static'),
    name='static'
)
