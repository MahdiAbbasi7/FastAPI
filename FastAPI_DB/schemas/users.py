from pydantic import BaseModel


# for validations database

class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

        # handel an instance of model sends to server like Dict
