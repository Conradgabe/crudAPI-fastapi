from pydantic import BaseModel

class UserBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class User(UserBase):
    id: int

    