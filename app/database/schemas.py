from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str
    
class UserGet(UserBase):
    token: str
    created_at: datetime
    modified_at: datetime
    status: str

class UserUpdate(UserBase):
    token : str | None = None
    modified_at: str | None = None
    status: str
    