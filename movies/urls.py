from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MovieViewSet

# Crear el router
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'movies', MovieViewSet)

# URLs de la app
urlpatterns = [
    path('', include(router.urls)),
] 