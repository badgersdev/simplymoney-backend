from ninja import Schema
from pydantic import EmailStr, model_validator
from typing import Optional, List
from datetime import datetime


class AnnouncementCreateEntrySchema(Schema):
    # data --> database
    email: EmailStr
    phone: str
    category: str
    location: str
    show_email: bool
    show_phone: bool
    label: str
    description: str
    exchange_type: str
    seller_type: str

    @model_validator(mode="after")
    def at_least_one_contact(self):
        if not self.show_email and not self.show_phone:
            raise ValueError(
                "You must provide at least an email or a phone number.")
        return self


# detail look
class AnnouncementDetailEntrySchema(Schema):
    id: int
    label: str
    description: str
    location: Optional[str] = None
    category: str
    exchange_type: str
    seller_type: str
    email: Optional[EmailStr]
    phone: Optional[str]
    show_email: bool
    show_phone: bool
    timestamp: datetime
    updated: datetime
    images: List[str] = []


# list look
class AnnouncementListEntrySchema(Schema):
    id: int
    label: str
    category: str
    location: Optional[str] = None
    exchange_type: str
    seller_type: str
    timestamp: datetime
    show_email: bool
    show_phone: bool
    images: List[str] = []


# response schema for Create Announcement
class CreateAnnouncementResponseSchema(Schema):
    message: str
    id: int
