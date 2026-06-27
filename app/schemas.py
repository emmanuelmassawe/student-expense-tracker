from datetime import date, datetime

from pydantic import BaseModel, EmailStr, Field


class ExpenseCreate(BaseModel):
    category: str = Field(..., examples=["food"])
    amount: float = Field(..., gt=0)
    expense_date: date


class ExpenseResponse(BaseModel):
    id: int
    student_id: int
    category: str
    amount: float
    expense_date: date
    created_at: datetime

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: str = "student"


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse