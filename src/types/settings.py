from pydantic import BaseSettings, SecretStr, PositiveInt, Field


class Settings(BaseSettings):
    SECRET_KEY: SecretStr
    EXPIRE_JWT: PositiveInt
    ALGORITHM: str = Field(default='HS256')
    TOKEN_TYPE: str = Field(default='Bearer')

    class Config:
        env_file = '.env'
