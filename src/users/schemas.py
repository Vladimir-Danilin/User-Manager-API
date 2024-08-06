from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field()


class UserUpdate(BaseModel):
    name: str = Field()
