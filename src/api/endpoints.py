from fastapi import HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from .router import router
from ..types import UserForm, Token
from ..database import User
from .dependecies import create_token, SETTINGS, auth


@router.post('/register')
async def register(form: UserForm):
    form.hash()
    async with User.session() as session:
        user = User(**form.dict())
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='email is not unique')
        else:
            raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail='success')


@router.post('/login', response_model=Token)
async def login(form: UserForm):
    async with User.session() as session:
        user = await session.scalar(
            select(User)
            .filter_by(email=form.email)
        )
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
    if not form.verify(user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid password')
    return Token(
        token_type=SETTINGS.TOKEN_TYPE,
        access_token=create_token(user.email)
    )


@router.get('/test')
async def test(user: User = Depends(auth)):
    return UserForm.from_orm(user)
