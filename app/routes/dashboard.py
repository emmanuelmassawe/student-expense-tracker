from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth import get_current_user, require_admin
from app.database import get_db
from app.models import MonthlySummary, StudentCluster, User

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/student/summary")
def get_my_monthly_summary(
    month: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    summary = (
        db.query(MonthlySummary)
        .filter(MonthlySummary.student_id == current_user.id)
        .filter(MonthlySummary.month == month)
        .first()
    )

    if not summary:
        raise HTTPException(
            status_code=404,
            detail="Monthly summary not found",
        )

    return {
        "student_id": summary.student_id,
        "month": summary.month,
        "food_expense": summary.food_expense,
        "rent": summary.rent,
        "transport": summary.transport,
        "education": summary.education,
        "entertainment": summary.entertainment,
        "savings": summary.savings,
        "total_spent": summary.total_spent,
        "remaining_balance": summary.remaining_balance,
    }


@router.get("/student/cluster")
def get_my_cluster_result(
    month: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    cluster = (
        db.query(StudentCluster)
        .filter(StudentCluster.student_id == current_user.id)
        .filter(StudentCluster.month == month)
        .first()
    )

    if not cluster:
        raise HTTPException(
            status_code=404,
            detail="Cluster result not found",
        )

    return {
        "student_id": cluster.student_id,
        "month": cluster.month,
        "cluster_label": cluster.cluster_label,
        "cluster_description": cluster.cluster_description,
    }


@router.get("/admin/summaries")
def get_all_monthly_summaries(
    month: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    summaries = (
        db.query(MonthlySummary)
        .filter(MonthlySummary.month == month)
        .all()
    )

    return summaries


@router.get("/admin/clusters")
def get_all_cluster_results(
    month: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    clusters = (
        db.query(StudentCluster)
        .filter(StudentCluster.month == month)
        .all()
    )

    return clusters