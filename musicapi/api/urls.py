from django.urls import path
from . import views

urlpatterns = [
	path('', views.APIRoot.as_view(), name='api-root'),
    path('generos/', views.GeneroMusicalListCreate.as_view(), name='genero-list-create'),
    path('artistas/', views.ArtistaListCreate.as_view(), name='artista-list-create'),
    path('albums/', views.AlbumListCreate.as_view(), name='album-list-create'),
    path('canciones/', views.CancionListCreate.as_view(), name='cancion-list-create'),
]