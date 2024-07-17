from rest_framework import serializers
from .models import GeneroMusical, Artista, Album, Cancion

class GeneroMusicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroMusical
        fields = '__all__'

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    generos = serializers.SlugRelatedField(
        many=True,
        slug_field='nombre',  # Nombre del campo que deseas usar
        queryset=GeneroMusical.objects.all()  # Queryset para obtener los objetos relacionados
    )
    artista = serializers.SlugRelatedField(
        slug_field='nombre',  # Nombre del campo que deseas usar
        queryset=Artista.objects.all()  # Queryset para obtener los objetos relacionados
    )    
    class Meta:
        model = Album
        fields = ['titulo', 'lanzamiento', 'artista', 'generos']

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'