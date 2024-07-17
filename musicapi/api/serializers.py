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
    class Meta:
        model = Album
        fields = '__all__'

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'