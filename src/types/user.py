from pydantic import BaseModel, EmailStr, Field, validator

from ..settings import pwd_context


class UserForm(BaseModel):
    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        regex=r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,64}'
    )

    def hash(self):
        self.password = pwd_context.hash(self.password)

    def verify(self, hashed_password: str) -> bool:
        return pwd_context.verify(self.password, hashed_password)

    class Config:
        orm_mode = True
