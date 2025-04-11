from typing import List

from pydantic import BaseModel, EmailStr, Field


class Contact(BaseModel):
    email: EmailStr
    phone: List[int] = Field(None, min_items=7, max_items=15)
