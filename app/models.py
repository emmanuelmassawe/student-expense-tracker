from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="student")
    created_at = Column(DateTime, default=datetime.utcnow)

    expenses = relationship("Expense", back_populates="student")
    monthly_summaries = relationship("MonthlySummary", back_populates="student")
    clusters = relationship("StudentCluster", back_populates="student")


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    expense_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("User", back_populates="expenses")


class MonthlySummary(Base):
    __tablename__ = "monthly_summaries"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    month = Column(String, nullable=False)

    food_expense = Column(Float, default=0)
    rent = Column(Float, default=0)
    transport = Column(Float, default=0)
    education = Column(Float, default=0)
    entertainment = Column(Float, default=0)
    savings = Column(Float, default=0)

    total_spent = Column(Float, default=0)
    remaining_balance = Column(Float, default=0)

    student = relationship("User", back_populates="monthly_summaries")


class StudentCluster(Base):
    __tablename__ = "student_clusters"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    month = Column(String, nullable=False)
    cluster_label = Column(Integer, nullable=False)
    cluster_description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("User", back_populates="clusters")