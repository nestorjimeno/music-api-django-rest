from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import GeneroMusical, Artista, Album, Cancion
from .serializers import GeneroMusicalSerializer, ArtistaSerializer, AlbumSerializer, CancionSerializer

class GeneroMusicalListCreate(generics.ListCreateAPIView):
    queryset = GeneroMusical.objects.all()
    serializer_class = GeneroMusicalSerializer

class ArtistaListCreate(generics.ListCreateAPIView):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class AlbumListCreate(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class CancionListCreate(generics.ListCreateAPIView):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer
    
class APIRoot(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'generos': reverse('genero-list-create', request=request),
            'artistas': reverse('artista-list-create', request=request),
            'albums': reverse('album-list-create', request=request),
            'canciones': reverse('cancion-list-create', request=request),
        })