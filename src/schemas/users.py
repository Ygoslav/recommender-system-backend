from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    id: int
    username: str


class UserCreateSchema(BaseModel):
    username: str
    password: str
