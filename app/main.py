from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routes import expenses, users
from app.routes import batch, expenses, users
from app.routes import batch, dashboard, expenses, users
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Expense Tracking System",
    description="A real-time and batch processing system for student expense analysis using K-Means clustering.",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="app/templates")
app.include_router(users.router)
app.include_router(expenses.router)
app.include_router(users.router)
app.include_router(expenses.router)
app.include_router(batch.router)

app.include_router(users.router)
app.include_router(expenses.router)
app.include_router(batch.router)
app.include_router(dashboard.router)


@app.get("/")
def home():
    return {
        "message": "Student Expense Tracking System API is running",
        "database": "PostgreSQL connected",
        "security": "User registration and login enabled",
    }




@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "student-expense-tracker",
    }

@app.get("/login-page")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
    )


@app.get("/student-dashboard-page")
def student_dashboard_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="student_dashboard.html",
    )


@app.get("/admin-dashboard-page")
def admin_dashboard_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="admin_dashboard.html",
    )

@app.get("/expense-form-page")
def expense_form_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="expense_form.html",
    )

@app.get("/register-page")
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
    )

@app.get("/index")
def index_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )

