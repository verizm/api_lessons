from enum import Enum
from pydantic import BaseModel, Field
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
    enabled: bool = Field(description="Rating participation flag")
    quality: int = Field(description="Quality rating")
    quantity: int = Field(description="Quantity rating")


class User(BaseModel):
    login: Optional[str] = Field(description="User login")
    roles: Optional[List[Roles]]
    medium_picture_url: str = Field(None, alias="mediumPictureUrl", description="Profile picture URL M-size")
    small_picture_url: str = Field(None, alias="smallPictureUrl", description="Profile picture URL S-size")
    status: str = Field(None, alias="User defined status")
    rating: Rating
    online: datetime = Field(None, description="Last seen online moment")
    name: str = Field(None, description="User real name")
    location: str = Field(None, description="User real location")
    registration: Optional[datetime] = Field(None, description="Date of registration")


class UserEnvelope(BaseModel):
    resource: Optional[User] = None
    metadata: Optional[str] = None
