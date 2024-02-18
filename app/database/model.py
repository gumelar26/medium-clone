import os
import enum
from datetime import datetime
from typing import Optional
from dotenv import load_dotenv

from sqlmodel import Field, SQLModel, create_engine

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

class Status(enum.Enum):
    ACTIVE = "active"
    INCATIVE = "inactive"

class User(SQLModel, table=True):
    email: str = Field(primary_key=True, index=True)
    username: str = Field(unique=True, index=True)
    password: str
    token: Optional[str] = None
    created_at: datetime = Field(default=datetime.now())
    modified_at: datetime = Field(default=datetime.now())
    status: Status = Field(default=Status.ACTIVE)
    
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_table()