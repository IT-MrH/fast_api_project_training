from re import search

from contact import Contact
from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self


class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
    contact: Contact

    @model_validator(mode='after')
    def validate_message(self) -> Self:
        pattern = r'\w*козявк*|\w*бяк*|\w*редиск*'
        if search(pattern, self.message):
            raise ValueError("Использование недопустимых слов")
        return self
