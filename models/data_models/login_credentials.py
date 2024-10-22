from pydantic import BaseModel, ConfigDict, Field


class LoginCredentials(BaseModel):
    model_config = ConfigDict(extra="forbid")
    login: str = Field(description="Login")
    password: str = Field(description="Password")
    remember_me: bool = Field(default=False, serialization_alias="rememberMe", description="Keep user session data")

