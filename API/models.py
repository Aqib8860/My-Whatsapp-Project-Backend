from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class User(BaseModel):
    name: str
    number: str
    email: str
    password: str
    generated_on: datetime = Field(default_factory=datetime.now)
    status: str = "Active"
