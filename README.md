## DEMO : https://student-expense-tracker-pdve.onrender.com/index

# 🎓 Student Expense Tracker

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Student Expense Tracker is a backend-focused personal finance management system designed to help students record income, track expenses, understand spending habits, and improve financial awareness.

The project is built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, and **python-dotenv**, following a clean **Layered Architecture** approach:

```text
Routes → Services → Models → Database
```

---

## 📌 Problem Statement

Many students face challenges managing their personal finances. They often receive money for school, rent, food, transport, learning materials, and daily needs, but may not have a clear way to track how that money is spent.

Common challenges include:

- Difficulty planning and following a budget
- Poor visibility into daily or monthly expenses
- Lack of awareness about spending habits
- Trouble identifying unnecessary or excessive spending
- Limited financial records for reviewing past behavior

Without a reliable tracking system, students may run out of money earlier than expected or fail to understand where their money is going.

---

## 💡 Solution Overview

Student Expense Tracker provides a structured system where students can record financial activity, categorize expenses, and review their spending patterns over time.

The application allows users to:

- Add and manage income records
- Add and categorize expenses
- View spending summaries
- Track financial behavior over time
- Store data securely in PostgreSQL
- Access API documentation through Swagger UI and ReDoc

The expected benefit is better financial awareness, improved budgeting habits, and easier monitoring of student spending behavior.

---

## 🎯 Project Objectives

- Build a secure backend API for student finance tracking
- Store income and expense data in a relational database
- Organize the project using layered architecture
- Use SQLAlchemy ORM for database interaction
- Use Alembic for database migrations
- Use environment variables for secure configuration
- Provide interactive API documentation for testing and development
- Create a professional, maintainable project suitable for portfolio and internship applications

---

## ✨ Key Features

- User account management
- Income tracking
- Expense tracking
- Expense categorization
- Spending history
- Financial summaries
- PostgreSQL database integration
- SQLAlchemy ORM models
- Alembic database migrations
- Environment-based configuration with `.env`
- Swagger UI documentation
- ReDoc documentation
- Layered architecture for clean code organization

---

## 🛠️ Technologies Used

| Category | Technology |
|---|---|
| Language | Python |
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Environment Variables | python-dotenv |
| API Documentation | Swagger UI, ReDoc |
| Server | Uvicorn |
| Architecture | Layered Architecture |

---

## 🏗️ System Architecture

The project follows a layered architecture where each part of the system has a clear responsibility.

```mermaid
flowchart LR
    User["User / Student"] --> Routes["API Routes"]
    Routes --> Services["Service Layer"]
    Services --> Models["SQLAlchemy Models"]
    Models --> Database["PostgreSQL Database"]
    Database --> Models
    Models --> Services
    Services --> Routes
    Routes --> User
```

### Architecture Layers

| Layer | Responsibility |
|---|---|
| Routes | Receive HTTP requests and return API responses |
| Services | Handle business logic and validation flow |
| Models | Define database tables using SQLAlchemy |
| Database | Store users, income, expenses, and related records |

---

## 📁 Folder Structure

```text
student-expense-tracker/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   │
│   ├── routes/
│   │   ├── users.py
│   │   ├── income.py
│   │   └── expenses.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   ├── income_service.py
│   │   └── expense_service.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── income.py
│   │   └── expense.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── income_schema.py
│   │   └── expense_schema.py
│   │
│   └── utils/
│
├── alembic/
│   └── versions/
│
├── alembic.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

> Note: Folder names may be adjusted depending on the final implementation, but the project should preserve the layered structure.

---

## 🗄️ Database Overview

The system uses PostgreSQL as the main database.

### Main Tables

| Table | Description |
|---|---|
| users | Stores student account information |
| income | Stores student income records |
| expenses | Stores student expense records |
| categories | Stores expense category information, if separated into its own table |

### Example Expense Categories

- Food
- Rent
- Transport
- Education
- Entertainment
- Savings
- Other

---

## 🔌 API Endpoints

Below is a sample API endpoint structure.

### User Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users/register` | Register a new user |
| POST | `/users/login` | Login user |
| GET | `/users/me` | Get current user profile |

### Income Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/income/` | Add income record |
| GET | `/income/` | Get income records |
| GET | `/income/{income_id}` | Get single income record |
| PUT | `/income/{income_id}` | Update income record |
| DELETE | `/income/{income_id}` | Delete income record |

### Expense Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/expenses/` | Add expense record |
| GET | `/expenses/` | Get expense records |
| GET | `/expenses/{expense_id}` | Get single expense record |
| PUT | `/expenses/{expense_id}` | Update expense record |
| DELETE | `/expenses/{expense_id}` | Delete expense record |

---

## ⚙️ Installation Instructions

### 1. Clone The Repository

```bash
git clone https://github.com/your-username/student-expense-tracker.git
cd student-expense-tracker
```

### 2. Create A Virtual Environment

```bash
python -m venv venv
```

### 3. Activate The Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables Setup

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/student_expense_db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

For GitHub, provide a safe example file named `.env.example`:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
SECRET_KEY=replace_with_your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Do not upload your real `.env` file to GitHub.

---

## 🧱 Database Migrations

Initialize Alembic if it has not already been configured:

```bash
alembic init alembic
```

Create a new migration:

```bash
alembic revision --autogenerate -m "create initial tables"
```

Apply migrations:

```bash
alembic upgrade head
```

---

## ▶️ Running The Application Locally

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

| Documentation | URL |
|---|---|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

---

## 🚀 Future Improvements

- Add frontend dashboard with charts and visual summaries
- Add JWT authentication and role-based access control
- Add monthly spending reports
- Add expense budget limits and alerts
- Add export to CSV or PDF
- Add analytics for spending trends
- Add automated tests with Pytest
- Add Docker support
- Add deployment instructions
- Add CI/CD pipeline using GitHub Actions

---

## 🤝 Contribution Guidelines

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add your feature"
```

5. Push to your branch

```bash
git push origin feature/your-feature-name
```

6. Open a pull request

Please keep contributions clear, focused, and well documented.

---

## 📄 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project for learning and portfolio purposes.

---

## 👤 Author

**Student Expense Tracker** was developed as a student-focused backend project for learning, portfolio development, and software engineering practice.

```text
Author: Your Name
GitHub: https://github.com/your-username
```

---

## ⭐ Project Status

This project is actively being developed and improved.

If you find this project useful, consider giving it a star on GitHub.
