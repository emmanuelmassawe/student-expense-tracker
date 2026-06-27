import pandas as pd
from sqlalchemy.orm import Session

from app.models import MonthlySummary

BOOM_AMOUNT = 600000


def import_monthly_csv(db: Session, csv_path: str, month: str):
    df = pd.read_csv(csv_path)

    required_columns = {
        "student_id",
        "food_expense",
        "rent",
        "transport",
        "education",
        "entertainment",
        "savings",
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    imported_rows = 0

    for _, row in df.iterrows():
        total_spent = (
            float(row["food_expense"])
            + float(row["rent"])
            + float(row["transport"])
            + float(row["education"])
            + float(row["entertainment"])
        )

        savings = float(row["savings"])
        remaining_balance = BOOM_AMOUNT - total_spent - savings

        existing_summary = (
            db.query(MonthlySummary)
            .filter(MonthlySummary.student_id == int(row["student_id"]))
            .filter(MonthlySummary.month == month)
            .first()
        )

        if existing_summary:
            existing_summary.food_expense = float(row["food_expense"])
            existing_summary.rent = float(row["rent"])
            existing_summary.transport = float(row["transport"])
            existing_summary.education = float(row["education"])
            existing_summary.entertainment = float(row["entertainment"])
            existing_summary.savings = savings
            existing_summary.total_spent = total_spent
            existing_summary.remaining_balance = remaining_balance
        else:
            summary = MonthlySummary(
                student_id=int(row["student_id"]),
                month=month,
                food_expense=float(row["food_expense"]),
                rent=float(row["rent"]),
                transport=float(row["transport"]),
                education=float(row["education"]),
                entertainment=float(row["entertainment"]),
                savings=savings,
                total_spent=total_spent,
                remaining_balance=remaining_balance,
            )

            db.add(summary)

        imported_rows += 1

    db.commit()

    return imported_rows