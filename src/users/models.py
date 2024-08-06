from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str = Field()
