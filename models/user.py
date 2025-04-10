from pydantic import BaseModel


class User(BaseModel):
    age: int
    name: str
    is_adult: bool = None
