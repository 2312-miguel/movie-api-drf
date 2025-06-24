# Project Introduction: Movie API DRF

This document provides an overview of the steps, commands, and key decisions made to create the Movie API DRF project.

---

## 1. Project Objective

Build a RESTful API for managing movies and categories using Django REST Framework, PostgreSQL, and Docker. The goal is to master DRF concepts such as serializers, viewsets, routers, and filtering.

---

## 2. Initial Setup

### a. Project Structure
- Created a new directory: `movie-api-drf`
- Added essential files: `Dockerfile`, `docker-compose.yml`, `requirements.txt`

### b. Docker & Dependencies
- Wrote a `Dockerfile` to use Python 3.11 and install dependencies
- Configured `docker-compose.yml` to run Django and PostgreSQL as separate services
- Added main dependencies to `requirements.txt`:
  - Django
  - djangorestframework
  - psycopg2-binary
  - django-filter
  - drf-spectacular

---

## 3. Project Creation & Configuration

### a. Create Django Project
```bash
docker-compose run web django-admin startproject config .
```

### b. Create Main App
```bash
docker-compose run web python manage.py startapp movies
```

### c. Register App
- Added `'movies'` to `INSTALLED_APPS` in `config/settings.py`

### d. Configure Database
- Set up PostgreSQL connection in `config/settings.py` using environment variables from `docker-compose.yml`

---

## 4. Models & Migrations

### a. Define Models
- Created `Category` and `Movie` models in `movies/models.py` with appropriate fields and relationships

### b. Run Migrations
```bash
docker-compose run web python manage.py makemigrations

docker-compose run web python manage.py migrate
```

---

## 5. Serializers
- Created `serializers.py` in the `movies` app
- Implemented `CategorySerializer`, `MovieSerializer`, and `MovieListSerializer` with custom validation

---

## 6. ViewSets & Routers
- Implemented `CategoryViewSet` and `MovieViewSet` in `movies/views.py` with CRUD, filtering, and custom actions
- Registered viewsets using DRF routers in `movies/urls.py`
- Included app URLs in `config/urls.py` under `/api/`

---

## 7. Filtering, Pagination, and Permissions
- Enabled filtering, search, and ordering in viewsets
- Configured pagination and permissions in `settings.py`

---

## 8. Automatic Documentation
- Integrated `drf-spectacular` for OpenAPI 3.0 documentation
- Added endpoints:
  - `/api/schema/` (OpenAPI schema)
  - `/api/docs/` (Swagger UI)
  - `/api/redoc/` (ReDoc)
- Enhanced documentation with `@extend_schema` decorators in viewsets

---

## 9. Useful Commands

- **Build containers:**
  ```bash
  docker-compose build
  ```
- **Start services:**
  ```bash
  docker-compose up -d
  ```
- **Run migrations:**
  ```bash
  docker-compose run web python manage.py migrate
  ```
- **Create superuser:**
  ```bash
  docker-compose run web python manage.py createsuperuser
  ```
- **Access API:**
  - Main: http://localhost:8000/api/
  - Admin: http://localhost:8000/admin/
  - Swagger UI: http://localhost:8000/api/docs/
  - ReDoc: http://localhost:8000/api/redoc/

---

## 10. Next Steps
- Add more tests and validations
- Implement authentication and permissions for advanced use cases
- Expand API features as needed

---

## 11. References
- [Django REST Framework](https://www.django-rest-framework.org/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/)
- [Docker Compose](https://docs.docker.com/compose/) 