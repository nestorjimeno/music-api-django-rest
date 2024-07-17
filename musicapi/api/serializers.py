from rest_framework import serializers
from .models import GeneroMusical, Artista, Album, Cancion

class GeneroMusicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroMusical
        fields = '__all__'

class ArtistaSerializer(serializers.ModelSerializer):
    generos = serializers.SlugRelatedField(
        many=True,
        slug_field='nombre',  # Nombre del campo que deseas usar
        queryset=GeneroMusical.objects.all()  # Queryset para obtener los objetos relacionados
    )
    
    class Meta:
        model = Artista
        fields = ['id', 'nombre', 'biografia', 'generos']

class AlbumSerializer(serializers.ModelSerializer):
    generos = serializers.SlugRelatedField(
        many=True,
        slug_field='nombre',  # Nombre del campo que deseas usar
        queryset=GeneroMusical.objects.all()  # Queryset para obtener los objetos relacionados
    )
    artistas = serializers.SlugRelatedField(
        many=True,
        slug_field='nombre',  # Nombre del campo que deseas usar
        queryset=Artista.objects.all()  # Queryset para obtener los objetos relacionados
    )    

    class Meta:
        model = Album
        fields = ['titulo', 'lanzamiento', 'artistas', 'generos']

class CancionSerializer(serializers.ModelSerializer):
    generos = serializers.SlugRelatedField(
        many=True,
        slug_field='nombre',  # Nombre del campo que deseas usar
        queryset=GeneroMusical.objects.all()  # Queryset para obtener los objetos relacionados
    )
    artistas = serializers.SlugRelatedField(
        many=True,
        slug_field='nombre',  # Nombre del campo que deseas usar
        queryset=Artista.objects.all()  # Queryset para obtener los objetos relacionados
    ) 
    album = serializers.SlugRelatedField(
        slug_field='titulo',  # Nombre del campo que deseas usar
        queryset=Album.objects.all()  # Queryset para obtener los objetos relacionados
    )

    class Meta:
        model = Cancion
        fields = ['id', 'titulo', 'album', 'artistas', 'duracion', 'generos', ]