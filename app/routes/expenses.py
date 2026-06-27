from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth import get_current_user

from app.database import get_db
from app.models import Expense, User
from app.schemas import ExpenseCreate, ExpenseResponse

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)

ALLOWED_CATEGORIES = {
    "food",
    "rent",
    "transport",
    "education",
    "entertainment",
    "savings",
}


@router.post("/", response_model=ExpenseResponse)
def create_expense(
    expense_data: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "student":
        raise HTTPException(
            status_code=403,
            detail="Only students can submit expenses",
        )

    if expense_data.category not in ALLOWED_CATEGORIES:
        raise HTTPException(
            status_code=400,
            detail="Invalid expense category",
        )

    expense = Expense(
        student_id=current_user.id,
        category=expense_data.category,
        amount=expense_data.amount,
        expense_date=expense_data.expense_date,
    )

    db.add(expense)
    db.commit()
    db.refresh(expense)

    return expense

@router.get("/", response_model=list[ExpenseResponse])
def get_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()


@router.get("/student/{student_id}", response_model=list[ExpenseResponse])
def get_student_expenses(student_id: int, db: Session = Depends(get_db)):
    return db.query(Expense).filter(Expense.student_id == student_id).all()