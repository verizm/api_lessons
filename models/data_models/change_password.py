from pydantic import BaseModel, Field, ConfigDict, UUID4


class ChangePassword(BaseModel):
    model_config = ConfigDict(extra="forbid")
    login: str = Field(description="Login")
    token: str = Field(description="Unique user authorize token uuid")
    old_password: str = Field(serialization_alias='oldPassword', description="Current pass")
    new_password: str = Field(serialization_alias='newPassword', description="New pass")
