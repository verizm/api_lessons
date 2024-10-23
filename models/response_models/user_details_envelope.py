from enum import Enum
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class Roles(str, Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNY_MODERATOR = "NannyModerator"
    REGULAR_MODERATOR = "RegularModerator"
    SENIOR_MODERATOR = "SeniorModerator"


class ParseMode(str, Enum):
    COMMON = "Common"
    InfoBdText = "Info"
    POST = "Post"
    CHAT = "Chat"


class ColorSchema(str, Enum):
    MODERN = "Modern"
    PALE = "Pale"
    CLASSIC = "Classic"
    CLASSIC_PALE = "ClassicPale"
    NIGHT = "Night"


class Rating(BaseModel):
    enabled: bool = Field(description="Rating participation flag")
    quality: int = Field(description="Quality rating")
    quantity: int = Field(description="Quantity rating")


class InfoBdText(BaseModel):
    value: str = Field(None, description="text")
    parseMode: List[ParseMode] = Field(description="BB text parse mode")


class PagingSettings(BaseModel):
    posts_per_page: int = Field(description="Number of posts on a game room page", validation_alias="postsPerPage")

    comments_per_page: int = Field(
        description="Number of commentaries on a game or a topic page",
        validation_alias="commentsPerPage",
    )
    topics_per_page: int = Field(description="Number of detached topics on a forum page", validation_alias="topicsPerPage")

    messages_per_page: int = Field(
        description="Number of private messages and conversations on dialogue page",
        validation_alias="messagesPerPage"
    )
    entities_per_page: int = Field(description="Number of other entities on page", validation_alias="entitiesPerPage")


class UserSettings(BaseModel):
    color_schema: ColorSchema = Field(validation_alias="colorSchema")
    nannyGreetingsMessage: str = Field(None, description="Message that user's newbies will receive once they are connected")
    paging: PagingSettings


class UserDetails(BaseModel):
    login: Optional[str] = Field(None, description="User login")
    roles: Optional[List[Roles]]
    medium_picture_url: str = Field(None, alias="mediumPictureUrl", description="Profile picture URL M-size")
    small_picture_url: str = Field(None, alias="smallPictureUrl", description="Profile picture URL S-size")
    status: str = Field(None, alias="User defined status")
    rating: Rating
    online: datetime = Field(None, alias="Last seen online moment")
    name: str = Field(None, alias="User real name")
    location: str = Field(None, alias="User real location")
    registration: datetime = Field(None, alias="User registration moment")
    icq: str = Field(None, description="User ICQ number")
    skype: str = Field(None, description="User Skype login")
    originalPictureUrl: str = Field(None, description="URL of profile picture original", validation_alias="originalPictureUrl")
    info: InfoBdText | str = None
    settings: UserSettings


class UserDetailsEnvelope(BaseModel):
    resource: UserDetails
    metadata: Optional[str] = None
