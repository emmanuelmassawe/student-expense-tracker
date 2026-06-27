import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sqlalchemy.orm import Session

from app.models import MonthlySummary, StudentCluster

FEATURE_COLUMNS = [
    "food_expense",
    "rent",
    "transport",
    "education",
    "entertainment",
    "savings",
]


def describe_cluster(row):
    values = {
        "food": row["food_expense"],
        "rent": row["rent"],
        "transport": row["transport"],
        "education": row["education"],
        "entertainment": row["entertainment"],
        "savings": row["savings"],
    }

    highest_category = max(values, key=values.get)

    if highest_category == "savings":
        return "High saver"

    if highest_category == "rent":
        return "High rent spender"

    if highest_category == "food":
        return "High food spender"

    if highest_category == "entertainment":
        return "High entertainment spender"

    if highest_category == "education":
        return "Education-focused spender"

    if highest_category == "transport":
        return "High transport spender"

    return "Balanced spender"


def run_kmeans_clustering(db: Session, month: str, number_of_clusters: int = 3):
    summaries = (
        db.query(MonthlySummary)
        .filter(MonthlySummary.month == month)
        .all()
    )

    if len(summaries) < number_of_clusters:
        raise ValueError(
            "Not enough student summaries for the requested number of clusters"
        )

    data = []

    for summary in summaries:
        data.append(
            {
                "student_id": summary.student_id,
                "food_expense": summary.food_expense,
                "rent": summary.rent,
                "transport": summary.transport,
                "education": summary.education,
                "entertainment": summary.entertainment,
                "savings": summary.savings,
            }
        )

    df = pd.DataFrame(data)

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[FEATURE_COLUMNS])

    model = KMeans(
        n_clusters=number_of_clusters,
        random_state=42,
        n_init=10,
    )

    df["cluster_label"] = model.fit_predict(scaled_features)

    saved_clusters = []

    for _, row in df.iterrows():
        cluster_description = describe_cluster(row)

        existing_cluster = (
            db.query(StudentCluster)
            .filter(StudentCluster.student_id == int(row["student_id"]))
            .filter(StudentCluster.month == month)
            .first()
        )

        if existing_cluster:
            existing_cluster.cluster_label = int(row["cluster_label"])
            existing_cluster.cluster_description = cluster_description
            saved_clusters.append(existing_cluster)
        else:
            student_cluster = StudentCluster(
                student_id=int(row["student_id"]),
                month=month,
                cluster_label=int(row["cluster_label"]),
                cluster_description=cluster_description,
            )

            db.add(student_cluster)
            saved_clusters.append(student_cluster)

    db.commit()

    for cluster in saved_clusters:
        db.refresh(cluster)

    return saved_clusters