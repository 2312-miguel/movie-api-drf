from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from django.http import JsonResponse
from .models import Category, Movie
from .serializers import CategorySerializer, MovieSerializer, MovieListSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Listar categorías",
        description="Obtiene una lista paginada de todas las categorías disponibles",
        tags=["categories"]
    ),
    create=extend_schema(
        summary="Crear categoría",
        description="Crea una nueva categoría de películas",
        tags=["categories"]
    ),
    retrieve=extend_schema(
        summary="Obtener categoría",
        description="Obtiene los detalles de una categoría específica",
        tags=["categories"]
    ),
    update=extend_schema(
        summary="Actualizar categoría",
        description="Actualiza completamente una categoría existente",
        tags=["categories"]
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente categoría",
        description="Actualiza parcialmente una categoría existente",
        tags=["categories"]
    ),
    destroy=extend_schema(
        summary="Eliminar categoría",
        description="Elimina una categoría existente",
        tags=["categories"]
    ),
)
class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo Category.
    Proporciona operaciones CRUD completas.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    ordering = ['name']  # Orden por defecto

    @extend_schema(
        summary="Obtener películas de categoría",
        description="Obtiene todas las películas que pertenecen a esta categoría",
        responses={200: MovieListSerializer(many=True)},
        tags=["categories"]
    )
    @action(detail=True, methods=['get'])
    def movies(self, request, pk=None):
        """
        Endpoint personalizado para obtener todas las películas de una categoría.
        URL: /api/categories/{id}/movies/
        """
        category = self.get_object()
        movies = category.movies.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        summary="Listar películas",
        description="Obtiene una lista paginada de todas las películas con filtros opcionales",
        parameters=[
            OpenApiParameter(
                name="year",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Filtrar por año de lanzamiento"
            ),
            OpenApiParameter(
                name="categories",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Filtrar por ID de categoría"
            ),
            OpenApiParameter(
                name="search",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Buscar en título y descripción"
            ),
            OpenApiParameter(
                name="ordering",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Ordenar por: title, year, duration, id (añadir - para descendente)"
            ),
        ],
        tags=["movies"]
    ),
    create=extend_schema(
        summary="Crear película",
        description="Crea una nueva película con sus categorías",
        tags=["movies"]
    ),
    retrieve=extend_schema(
        summary="Obtener película",
        description="Obtiene los detalles completos de una película específica",
        tags=["movies"]
    ),
    update=extend_schema(
        summary="Actualizar película",
        description="Actualiza completamente una película existente",
        tags=["movies"]
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente película",
        description="Actualiza parcialmente una película existente",
        tags=["movies"]
    ),
    destroy=extend_schema(
        summary="Eliminar película",
        description="Elimina una película existente",
        tags=["movies"]
    ),
)
class MovieViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo Movie.
    Proporciona operaciones CRUD completas con filtros avanzados.
    """
    queryset = Movie.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['year', 'categories']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'year', 'duration', 'id']
    ordering = ['-year', 'title']  # Orden por defecto: año descendente, luego título

    def get_serializer_class(self):
        """
        Usa MovieListSerializer para listar y MovieSerializer para el resto.
        """
        if self.action == 'list':
            return MovieListSerializer
        return MovieSerializer

    @extend_schema(
        summary="Películas recientes",
        description="Obtiene las películas lanzadas desde el año 2020",
        responses={200: MovieListSerializer(many=True)},
        tags=["movies"]
    )
    @action(detail=False, methods=['get'])
    def recent(self, request):
        """
        Endpoint personalizado para obtener las películas más recientes.
        URL: /api/movies/recent/
        """
        recent_movies = Movie.objects.filter(year__gte=2020).order_by('-year', 'title')
        serializer = self.get_serializer(recent_movies, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Películas largas",
        description="Obtiene las películas con duración mayor a 120 minutos",
        responses={200: MovieListSerializer(many=True)},
        tags=["movies"]
    )
    @action(detail=False, methods=['get'])
    def long_movies(self, request):
        """
        Endpoint personalizado para obtener películas largas (>120 minutos).
        URL: /api/movies/long_movies/
        """
        long_movies = Movie.objects.filter(duration__gt=120).order_by('-duration', 'title')
        serializer = self.get_serializer(long_movies, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Añadir categoría a película",
        description="Añade una categoría existente a una película específica",
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'category_id': {
                        'type': 'integer',
                        'description': 'ID de la categoría a añadir'
                    }
                },
                'required': ['category_id']
            }
        },
        responses={
            200: MovieSerializer,
            400: {'type': 'object', 'properties': {'error': {'type': 'string'}}},
            404: {'type': 'object', 'properties': {'error': {'type': 'string'}}}
        },
        tags=["movies"]
    )
    @action(detail=True, methods=['post'])
    def add_category(self, request, pk=None):
        """
        Endpoint personalizado para añadir una categoría a una película.
        URL: /api/movies/{id}/add_category/
        """
        movie = self.get_object()
        category_id = request.data.get('category_id')
        
        if not category_id:
            return Response(
                {'error': 'category_id es requerido'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            category = Category.objects.get(id=category_id)
            movie.categories.add(category)
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(
                {'error': 'Categoría no encontrada'}, 
                status=status.HTTP_404_NOT_FOUND
            )
