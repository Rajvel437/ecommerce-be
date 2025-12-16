🛒 Ecommerce Backend API (FastAPI)

A scalable and modular Ecommerce Backend API built using FastAPI, following clean architecture principles with clear separation of concerns (routes, services, schemas, models, and database layer).

🚀 Tech Stack

Backend Framework: FastAPI

Language: Python 3.10+

Database: SQL Server (via SQLAlchemy)

ORM: SQLAlchemy

API Docs: Swagger (OpenAPI)

Environment Management: Python-dotenv

Version Control: Git & GitHub

📁 Project Structure
ecommerce/
│
├── app/
│   ├── core/
│   │   └── dependencies.py        # Common dependencies (DB, auth, etc.)
│   │
│   ├── database/
│   │   └── mssql.py                # SQL Server connection & session
│   │
│   ├── models/                     # SQLAlchemy ORM models
│   │
│   ├── routes/
│   │   └── api/
│   │       └── v1/
│   │           └── endpoints/
│   │               ├── auth.py     # Authentication routes
│   │               └── user.py     # User-related routes
│   │
│   ├── schemas/
│   │   └── users.py                # Pydantic schemas
│   │
│   ├── services/
│   │   ├── auth.service.py         # Authentication business logic
│   │   └── user.py                 # User business logic
│   │
│   ├── config.py                   # App & environment configuration
│   └── main.py                     # FastAPI application entry point
│
├── .env                            # Environment variables (ignored in git)
├── .gitignore
├── README.md
└── .venv/

✨ Key Features

✅ User Registration & Authentication

✅ Layered architecture (Routes → Services → DB)

✅ Async-ready FastAPI endpoints

✅ Clean separation of concerns

✅ Swagger & ReDoc auto-generated docs

✅ Environment-based configuration

✅ Production-ready project structure

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Rajvel437/ecommerce-be.git
cd ecommerce

2️⃣ Create & Activate Virtual Environment
python -m venv .venv


Windows

.venv\Scripts\activate


Linux / Mac

source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the root directory:

DB_SERVER=localhost
DB_NAME=ecommerce_db
DB_USER=sa
DB_PASSWORD=your_password


⚠️ .env is ignored by Git for security reasons.

5️⃣ Run the Application
uvicorn app.main:app --host 0.0.0.0 --port 8002 --reload

📄 API Documentation

Once the server is running:

Swagger UI 👉 http://localhost:8002/docs

ReDoc 👉 http://localhost:8002/redoc

🧠 Architecture Overview
Client
  ↓
Routes (FastAPI)
  ↓
Services (Business Logic)
  ↓
Database Layer (SQLAlchemy)


This structure ensures:

Maintainability

Testability

Scalability

🔀 Git Workflow

main → Production-ready code

raj/dev → Development branch

Feature Development Flow:
git checkout -b raj/dev
git add .
git commit -m "Add feature"
git push -u origin raj/dev


Create a Pull Request → merge into main.

🛡️ Best Practices Followed

❌ No secrets in code

❌ No .env committed

✅ Modular service-based design

✅ Clear API versioning (/api/v1)

✅ Industry-standard Git workflow

📌 Future Enhancements

🔐 JWT Authentication

🧾 Product & Order Management

💳 Payment Gateway Integration

🐳 Dockerization

☁️ Cloud Deployment (Render / AWS)

👨‍💻 Author

Rajvel R
Backend Developer | FastAPI | Python

🔗 GitHub: https://github.com/Rajvel437

⭐ Final Note (Important)

This project structure and workflow matches real-world production standards
and is highly suitable for interviews and scalable systems.
