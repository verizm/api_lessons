from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
)


class LoginCredentials(BaseModel):
    model_config = ConfigDict(extra="forbid")

    login: str = Field(description="Login")
    password: str = Field(description="Password")
    remember_me: bool = Field(default=False, description="remember user settings", serialization_alias="rememberMe")
