from pydantic import BaseModel


class PostV1AccountsPasswordRequest(BaseModel):
    login: str
    email: str
