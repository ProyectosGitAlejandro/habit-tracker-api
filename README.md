# Habit Tracker API

REST API for tracking personal habits, daily completions, and user productivity analytics.

The project was built with Django and Django REST Framework following a modular architecture and separating business logic into service layers.

## Tech Stack

* Python
* Django
* Django REST Framework
* JWT Authentication (SimpleJWT)
* drf-spectacular (OpenAPI documentation)
* SQLite (development)

The project structure is compatible with PostgreSQL for production environments.

## Features

### Authentication

JWT authentication is used for securing the API.

Endpoints:

POST /api/auth/login
POST /api/auth/refresh

### Habits

Users can create and manage personal habits.

Endpoints:

GET /api/habits/
POST /api/habits/
PUT /api/habits/{id}/
DELETE /api/habits/{id}/

Features implemented:

* user-scoped data
* filtering
* search
* ordering
* pagination

### Habit Logs

Habit completion is recorded using logs.

Endpoints:

GET /api/logs/
POST /api/logs/

Each log represents the completion state of a habit for a specific date.

### Analytics

Basic productivity analytics are provided through a dedicated endpoint.

Endpoint:

GET /api/analytics/

Example response:

{
"total_habits": 5,
"completed_today": 3,
"completion_rate": 60,
"consistency_score": 70
}

Metrics included:

* total habits
* habits completed today
* completion rate
* 30-day consistency score

### Heatmap Data

Endpoint:

GET /api/analytics/heatmap/

Returns activity data for the last 365 days.
This data can be used to build contribution-style heatmaps similar to GitHub activity charts.

Example:

[
{"date": "2026-03-10", "count": 2},
{"date": "2026-03-11", "count": 1},
{"date": "2026-03-12", "count": 0}
]

## API Documentation

OpenAPI documentation is available through:

/api/docs/

The schema is generated automatically using drf-spectacular.

## Tests

Basic API tests are included for:

* habit creation
* habit logs
* analytics endpoints

Run the test suite with:

python manage.py test

## Installation

Clone the repository:

git clone https://github.com/ProyectosGitAlejandro/habit-tracker-api.git

Navigate to the backend directory:

cd habit-tracker-api/backend

Create virtual environment:

python -m venv venv

Activate environment:

Windows:
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start the development server:

python manage.py runserver

## Project Structure

backend/

analytics/
habits/
logs/
users/
config/

Business logic related to analytics and statistics is implemented inside a service layer (`analytics/services.py`).

## Notes

The project was developed as a backend-focused exercise to practice building REST APIs with Django REST Framework, including authentication, analytics endpoints, filtering, and automated tests.
