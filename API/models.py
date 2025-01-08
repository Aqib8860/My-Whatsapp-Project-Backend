from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class User(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    country: str
    state: str
    phone: str
    email: str
    password: str
    generated_on: datetime = Field(default_factory=datetime.now)
    status: str = "Active"
