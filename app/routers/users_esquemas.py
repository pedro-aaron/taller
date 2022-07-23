from pydantic import BaseModel, Field
from typing import Union


class RequestCreateUser(BaseModel):
    username: str
    full_name: str
    email: Union[str, None] = None
    phone: str


class ResponseCreateUser(RequestCreateUser):
    id: str = Field(..., alias="_id")
