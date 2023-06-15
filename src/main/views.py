from starlette.requests import Request

from .router import router
from ..settings import templating


@router.get('/register')
async def register(request: Request):
    return templating.TemplateResponse(
        name='main/index.html',
        context={
            'request': request
        }
    )
