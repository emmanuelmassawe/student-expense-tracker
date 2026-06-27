from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import require_admin
from app.database import get_db
from app.ml.aggregate import aggregate_monthly_expenses
from app.models import User


from fastapi import HTTPException
from app.ml.import_monthly_csv import  import_monthly_csv
from app.ml.clustering import run_kmeans_clustering

router = APIRouter(
    prefix="/batch",
    tags=["Batch Processing"],
)


@router.post("/aggregate/monthly")
def run_monthly_aggregation(
    year: int,
    month: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    summaries = aggregate_monthly_expenses(db=db, year=year, month=month)

    return {
        "message": "Monthly aggregation completed",
        "year": year,
        "month": month,
        "students_processed": len(summaries),
    }

@router.post("/cluster/monthly")
def run_monthly_clustering(
    month: str,
    number_of_clusters: int = 3,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    try:
        clusters = run_kmeans_clustering(
            db=db,
            month=month,
            number_of_clusters=number_of_clusters,
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    return {
        "message": "K-Means clustering completed",
        "month": month,
        "number_of_clusters": number_of_clusters,
        "students_clustered": len(clusters),
    }

@router.post("/import/monthly-csv")
def import_existing_monthly_csv(
    month: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    csv_path = "data/student_expenses.csv"

    try:
        imported_rows = import_monthly_csv(
            db=db,
            csv_path=csv_path,
            month=month,
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    return {
        "message": "Monthly CSV imported successfully",
        "month": month,
        "rows_imported": imported_rows,
        "destination_table": "monthly_summaries",
    }