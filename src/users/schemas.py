from pydantic import BaseModel, EmailStr, model_validator
from ninja import Schema


class UserSignupSchema(Schema):
    email: EmailStr
    password: str

    @model_validator(mode="after")
    def validate_password(self):
        if len(self.password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        return self
