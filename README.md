# Habit Tracker API

A professional REST API for tracking personal habits, daily completions, and productivity analytics.

This project was built using **Django** and **Django REST Framework**, following a clean architecture with service layers, analytics endpoints, and automated testing.

---

# 🚀 Features

## Authentication

JWT-based authentication using **SimpleJWT**

Endpoints:

POST /api/auth/login
POST /api/auth/refresh

---

## Habits Management

Users can create and manage personal habits.

Endpoints:

GET /api/habits
POST /api/habits
PUT /api/habits/{id}
DELETE /api/habits/{id}

Features:

* User scoped data
* Filtering
* Search
* Ordering
* Pagination

---

## Habit Logs

Users can log daily habit completions.

Endpoints:

GET /api/logs
POST /api/logs

Each log represents a completed habit on a specific date.

---

## Streak Calculation

Each habit includes:

* current_streak
* longest_streak

These values are calculated dynamically using the service layer.

---

## Analytics

The API provides productivity insights for each user.

Endpoint:

GET /api/analytics/

Example response:

{
"total_habits": 5,
"completed_today": 3,
"completion_rate": 60,
"consistency_score": 70
}

Metrics include:

* Total habits
* Habits completed today
* Daily completion rate
* 30-day consistency score

---

## Heatmap Analytics

Endpoint:

GET /api/analytics/heatmap/

Returns daily activity data for the last 365 days.

This can be used to generate a **GitHub-style contribution heatmap**.

Example:

[
{ "date": "2026-03-10", "count": 2 },
{ "date": "2026-03-11", "count": 1 },
{ "date": "2026-03-12", "count": 0 }
]

---

# 📊 Additional Analytics Services

The project also includes service functions for:

* Weekly completion statistics
* Monthly productivity trends
* Best performing habits

These can be used for dashboards or productivity charts.

---

# 🧪 Automated Testing

The project includes API tests for:

* Habit creation
* Habit logs
* Analytics endpoints

Run tests with:

python manage.py test

---

# 📑 API Documentation

Interactive documentation is available using OpenAPI.

Access it at:

/api/docs/

---

# 🏗️ Project Architecture

habit-tracker
│
├── backend
│   ├── config
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   ├── users
│   ├── habits
│   ├── logs
│   ├── analytics
│
└── README.md

Key architectural patterns:

* Service Layer for business logic
* Modular Django apps
* JWT Authentication
* RESTful API design

---

# 🛠️ Tech Stack

Backend:

* Python 3.12
* Django
* Django REST Framework
* SimpleJWT
* drf-spectacular

Database:

* SQLite (development)
* Compatible with PostgreSQL

---

# ⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/habit-tracker.git

Navigate to the backend:

cd habit-tracker/backend

Create virtual environment:

python -m venv venv

Activate environment:

Windows:
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start server:

python manage.py runserver

---

# 🔐 Environment Variables

Create a `.env` file in the backend folder.

Example:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

---

# 📌 Future Improvements

Possible improvements:

* Habit reminders
* Notifications
* Social habit sharing
* Public habit dashboards
* Frontend dashboard (React)

---

# 👨‍💻 Author

Alejandro

Backend project built to practice building scalable APIs with Django REST Framework.
