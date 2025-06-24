# Movie API DRF

REST API for movie management, developed with Django and Django REST Framework, using PostgreSQL as the database and Docker for deployment.

## Technologies
- Python 3.11
- Django 4.2
- Django REST Framework
- PostgreSQL 14
- Docker & Docker Compose
- django-filter
- drf-spectacular (OpenAPI documentation)

## Description
Provides CRUD operations for movies, manages categories, and allows advanced filtering. Ideal for learning and mastering Django REST Framework (serializers, viewsets, routers, filters).

## Quick Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
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

5. **Create a superuser (optional):**
   ```bash
   docker-compose run web python manage.py createsuperuser
   ```

6. **Access the API:**
   - API: http://localhost:8000/api/
   - Admin: http://localhost:8000/admin/
   - Authentication: http://localhost:8000/api-auth/

## Automatic Documentation (OpenAPI)

- **Swagger UI:** [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- **ReDoc:** [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)
- **JSON Schema:** [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

Documentation is automatically generated with [drf-spectacular](https://drf-spectacular.readthedocs.io/).

## Environment Variables
Database environment variables are defined in `docker-compose.yml`.

## Recommended Structure
- `config/` - Django project
- `movies/` - Main app (movies, categories)

## Completed and Pending Tasks
See [`TASKS.md`](TASKS.md) for completed and pending tasks.

---

## License
MIT 