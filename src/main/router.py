from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter(
    default_response_class=HTMLResponse
)
