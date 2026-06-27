from datetime import date

from sqlalchemy.orm import Session

from app.models import Expense, MonthlySummary, User

BOOM_AMOUNT = 600000

EXPENSE_CATEGORIES = {
    "food": "food_expense",
    "rent": "rent",
    "transport": "transport",
    "education": "education",
    "entertainment": "entertainment",
    "savings": "savings",
}


def aggregate_monthly_expenses(db: Session, year: int, month: int):
    month_start = date(year, month, 1)

    if month == 12:
        month_end = date(year + 1, 1, 1)
    else:
        month_end = date(year, month + 1, 1)

    students = db.query(User).filter(User.role == "student").all()
    summaries = []

    for student in students:
        expenses = (
            db.query(Expense)
            .filter(Expense.student_id == student.id)
            .filter(Expense.expense_date >= month_start)
            .filter(Expense.expense_date < month_end)
            .all()
        )

        totals = {
            "food_expense": 0,
            "rent": 0,
            "transport": 0,
            "education": 0,
            "entertainment": 0,
            "savings": 0,
        }

        for expense in expenses:
            summary_field = EXPENSE_CATEGORIES.get(expense.category)

            if summary_field:
                totals[summary_field] += expense.amount

        total_spent = (
            totals["food_expense"]
            + totals["rent"]
            + totals["transport"]
            + totals["education"]
            + totals["entertainment"]
        )

        # Savings is treated as money kept aside, not spending.
        remaining_balance = BOOM_AMOUNT - total_spent - totals["savings"]

        month_label = f"{year}-{month:02d}"

        existing_summary = (
            db.query(MonthlySummary)
            .filter(MonthlySummary.student_id == student.id)
            .filter(MonthlySummary.month == month_label)
            .first()
        )

        if existing_summary:
            existing_summary.food_expense = totals["food_expense"]
            existing_summary.rent = totals["rent"]
            existing_summary.transport = totals["transport"]
            existing_summary.education = totals["education"]
            existing_summary.entertainment = totals["entertainment"]
            existing_summary.savings = totals["savings"]
            existing_summary.total_spent = total_spent
            existing_summary.remaining_balance = remaining_balance
            summaries.append(existing_summary)
        else:
            summary = MonthlySummary(
                student_id=student.id,
                month=month_label,
                food_expense=totals["food_expense"],
                rent=totals["rent"],
                transport=totals["transport"],
                education=totals["education"],
                entertainment=totals["entertainment"],
                savings=totals["savings"],
                total_spent=total_spent,
                remaining_balance=remaining_balance,
            )
            db.add(summary)
            summaries.append(summary)

    db.commit()

    for summary in summaries:
        db.refresh(summary)

    return summaries