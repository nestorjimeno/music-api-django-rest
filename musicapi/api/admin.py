from django.contrib import admin
from .models import GeneroMusical, Artista, Album, Cancion

@admin.register(GeneroMusical)
class GeneroMusicalAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'genero']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'artista', 'lanzamiento', 'mostrar_generos']

    def mostrar_generos(self, obj):
        return ", ".join([genero.nombre for genero in obj.generos.all()])

    mostrar_generos.short_description = 'Géneros'

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'album', 'duracion']