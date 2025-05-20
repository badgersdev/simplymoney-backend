from ninja import Schema
from datetime import datetime
from pydantic import EmailStr


class WaitlistCreateEntrySchema(Schema):
    # Create -> Data
    # entry IN
    email: EmailStr
    label: str
    amount: float


class WaitlistListEntrySchema(Schema):
    # LIST -> Data
    # WaitlistEntryOut
    id: int
    label: str
    email: EmailStr
    amount: float
    timestamp: datetime


class WaitlistDetailEntrySchema(Schema):
    # GET -> Data
    # WaitlistEntryOut
    email: str
    amount: float
    label: str
    timestamp: datetime
    updated: datetime
