from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import List, Optional


class Roles(str, Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNY_MODERATOR = "NannyModerator"
    REGULAR_MODERATOR = "RegularModerator"
    SENIOR_MODERATOR = "SeniorModerator"


class Rating(BaseModel):
    enabled: bool = Field(description="Enabled")
    quality: int = Field(description="Quality")
    quantity: int = Field(description="Quantity")


class User(BaseModel):
    login: str = Field(description="Login")
    roles: List[Roles]
    medium_picture_url: str = Field(None, alias="mediumPictureUrl")
    small_picture_url: str = Field(None, alias="smallPictureUrl")
    status: str = Field(None, alias="status")
    rating: Rating
    online: datetime = Field(None, alias="online")
    name: str = Field(None, alias="name")
    location: str = Field(None, alias="location")
    registration: datetime


class Model(BaseModel):
    resource: Optional[User] = None
    metadata: Optional[str] = None
