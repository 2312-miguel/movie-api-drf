from rest_framework import serializers
from .models import Category, Movie


class CategorySerializer(serializers.ModelSerializer):
    """Serializer para el modelo Category"""
    
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']


class MovieSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Movie"""
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True, 
        write_only=True, 
        queryset=Category.objects.all(),
        source='categories',
        required=False
    )
    
    class Meta:
        model = Movie
        fields = [
            'id', 
            'title', 
            'description', 
            'year', 
            'duration', 
            'categories',
            'category_ids'
        ]
        read_only_fields = ['id']
    
    def validate_year(self, value):
        """Validación personalizada para el año"""
        if value < 1888:  # Año de la primera película
            raise serializers.ValidationError("El año debe ser mayor a 1888")
        if value > 2030:  # Año futuro razonable
            raise serializers.ValidationError("El año no puede ser mayor a 2030")
        return value
    
    def validate_duration(self, value):
        """Validación personalizada para la duración"""
        if value < 1:
            raise serializers.ValidationError("La duración debe ser mayor a 0 minutos")
        if value > 600:  # 10 horas máximo
            raise serializers.ValidationError("La duración no puede ser mayor a 600 minutos")
        return value


class MovieListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listar películas"""
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'duration', 'categories'] 