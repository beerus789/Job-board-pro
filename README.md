# FastAPI To-Do App (Async, PostgreSQL, SQLModel)

Welcome to a **Production-Ready, High-Performance To-Do API** built with FastAPI, SQLModel, and PostgreSQL! This project is designed for both beginners and advanced users, featuring a beautiful, interactive API UI and scalable async backend.

---

## 🚀 Features
- **Async CRUD API**: All endpoints use Python async for maximum performance and scalability.
- **Handles 1000s of Users**: Thanks to async and FastAPI, this API can handle hundreds or thousands of concurrent users (limited only by your server and DB hardware).
- **PostgreSQL with asyncpg**: Fast, production-grade database access.
- **SQLModel**: Combines Pydantic validation and SQLAlchemy ORM for robust data handling.
- **Docker Compose**: Instantly spin up a local PostgreSQL database.
- **Interactive Swagger UI**: Test and explore the API visually at `/docs`—no frontend code needed!
- **Beginner-Friendly**: Clear code, comments, and step-by-step instructions.
- **Easily Extensible**: Add authentication, user management, or a custom frontend.

---

## 🌈 UI Experience
- **Swagger UI** at `/docs` is your playground! Add, view, update, and delete To-Do items with a few clicks.
- **Try it out**: Each endpoint has a "Try it out" button—no need for Postman or curl.
- **Live feedback**: See responses, errors, and data instantly.
- **Perfect for demos, learning, and prototyping.**

---

## 🏗️ Architecture & Scalability
- **Async Endpoints**: All database and API operations are async, so the app can serve many users at once without blocking.
- **Production-Ready**: Swap the database URL for a cloud PostgreSQL instance and deploy to any cloud provider.
- **Scalable**: Add more endpoints, models, or even a React/Vue frontend easily.
- **Extensible**: Add JWT authentication, rate limiting, or background tasks as needed.

---

## 📈 What Can Be Improved or Added?
- **Custom Frontend**: Build a React, Vue, or Svelte UI for a modern web app experience.
- **User Authentication**: Add login/signup and user-specific To-Do lists.
- **Task Deadlines & Reminders**: Add due dates, notifications, or recurring tasks.
- **Admin Dashboard**: Monitor usage, stats, and manage users/tasks.
- **API Rate Limiting**: Protect your API from abuse.
- **Deployment**: Use Docker Compose for full-stack deployment (API + DB + frontend).

---

## 📂 Folder Structure
```
day_2_fast_api/
├── config.py         # Environment/config management
├── crud/             # CRUD logic (async)
├── database.py       # Async DB engine/session
├── docker-compose.yml# PostgreSQL setup
├── main.py           # FastAPI app
├── models/           # Data models
├── requirements.txt  # Python dependencies
└── .env              # Environment variables
```

---

## 🛠️ Quick Start

### 1. Clone the repository and navigate to the project folder
```
git clone <your-repo-url>
cd <project-folder>/day_2_fast_api
```

### 2. Set up and activate a virtual environment
```
python -m venv venv
venv\Scripts\Activate.ps1  # On PowerShell
# or
venv\Scripts\activate.bat  # On cmd
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Start PostgreSQL with Docker
```
docker compose -f "docker-compose.yml" up -d --build
```

### 5. Set environment variable (Windows PowerShell)
If `.env` is not picked up automatically, run:
```
$env:DATABASE_URL="postgresql://user:password@localhost:5432/tododb"
```

### 6. Run the FastAPI app
From the parent directory (where `day_2_fast_api` is a folder):
```
uvicorn day_2_fast_api.main:app --reload
```

### 7. Open the API docs
Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser. You can interact with the API (add, view, update, delete To-Do items) using the Swagger UI.

---

## 🔗 API Endpoints
- `GET /` — Welcome message
- `POST /todos/` — Create a new To-Do
- `GET /todos/` — List all To-Dos
- `GET /todos/{todo_id}` — Get a To-Do by ID
- `PUT /todos/{todo_id}` — Update a To-Do
- `DELETE /todos/{todo_id}` — Delete a To-Do

---

## 👩‍💻 For Beginners
- All code is commented for clarity.
- Uses modern async Python best practices.
- No frontend code is needed—just use the built-in docs UI.
- If you get stuck, check the terminal for error messages and follow the instructions above.

---

## 🧑‍🤝‍🧑 How many users can it handle?
- With async endpoints and a proper PostgreSQL setup, this API can handle hundreds or thousands of concurrent users (limited by your server resources).
- For even more scalability, deploy behind a production ASGI server like Uvicorn or Hypercorn with multiple workers.

---

## 🛠️ Troubleshooting
- If you see `DATABASE_URL` errors, set the environment variable manually as shown above.
- Make sure Docker Desktop is running before starting the app.
- If you get import errors, run `uvicorn` from the parent directory and use the full module path.

---
