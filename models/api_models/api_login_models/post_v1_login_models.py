from pydantic import BaseModel


class PostV1LoginRequest(BaseModel):
    login: str
    password: str
    rememberMe: bool = False
