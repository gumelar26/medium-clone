from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str
    
class UserGet(UserBase):
    token: str | None
    created_at: datetime
    modified_at: datetime
    status: str

class UserUpdate(UserBase):
    password: str
    token : str | None
    modified_at: str
    status: str
    