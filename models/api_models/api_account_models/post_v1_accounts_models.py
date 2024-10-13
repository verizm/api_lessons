from pydantic import BaseModel
from typing import List


class PostV1AccountsRequest(BaseModel):
    login: str
    email: str
    password: str


class PostV1AccountsResponse(BaseModel):
    type: str
    title: str
    status: int
    traceId: str

