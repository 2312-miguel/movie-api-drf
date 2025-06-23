# Movie API DRF

REST API for movie management, developed with Django and Django REST Framework, using PostgreSQL as the database and Docker for deployment.

## Technologies
- Python 3.11
- Django 4.2
- Django REST Framework
- PostgreSQL 14
- Docker & Docker Compose
- django-filter

## Description
Provides CRUD operations for movies, manages categories, and allows advanced filtering. Built with Django REST Framework (serializers, viewsets, routers, filters).

## Quick Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/2312-miguel/movie-api-drf.git
   cd movie-api-drf
   ```

2. **Build the containers:**
   ```bash
   docker-compose build
   ```

3. **Start the services:**
   ```bash
   docker-compose up -d
   ```

4. **Apply migrations:**
   ```bash
   docker-compose run web python manage.py migrate
   ```

5. **Access the API:**
   - API: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

## Environment Variables
Database environment variables are defined in `docker-compose.yml`.

## Completed and Pending Tasks
See [`TASKS.md`](TASKS.md) for completed and pending tasks.

---

## License
MIT 