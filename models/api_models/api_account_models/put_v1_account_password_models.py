from pydantic import BaseModel, Field


class PutV1AccountsPasswordRequest(BaseModel):
    login: str
    token: str
    old_password: str = Field(serialization_alias='oldPassword')
    new_password: str = Field(serialization_alias='newPassword')