from datetime import datetime, timedelta
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class MemberCreate(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1)


class MemberOut(BaseModel):
    id: int
    email: str
    name: str
    status: str

    model_config = {"from_attributes": True}


class BookCreate(BaseModel):
    isbn: str
    title: str
    author: str


class BookOut(BaseModel):
    id: int
    isbn: str
    title: str
    author: str

    model_config = {"from_attributes": True}


class LoanCreate(BaseModel):
    member_id: int
    book_id: int
    days: int = Field(default=14, ge=1, le=90)


class LoanOut(BaseModel):
    id: int
    member_id: int
    book_id: int
    status: str
    due_at: datetime

    model_config = {"from_attributes": True}


class LoanListResponse(BaseModel):
    loans: List[LoanOut]


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
