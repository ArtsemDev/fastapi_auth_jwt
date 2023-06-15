from passlib.context import CryptContext
from fastapi.templating import Jinja2Templates

from .types import Settings


SETTINGS = Settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
templating = Jinja2Templates(directory='templates')
