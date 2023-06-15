from sqlalchemy import Column, VARCHAR, INT
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Base(DeclarativeBase):
    _engine = create_async_engine('sqlite+aiosqlite:///db.sqlite3')
    session = async_sessionmaker(bind=_engine)


class User(Base):
    __tablename__ = 'user'

    id = Column(INT, primary_key=True, autoincrement=True)
    email = Column(VARCHAR(128), nullable=False, unique=True)
    password = Column(VARCHAR(256), nullable=False)
