from django.contrib import admin
from .models import GeneroMusical, Artista, Album, Cancion

@admin.register(GeneroMusical)
class GeneroMusicalAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'mostrar_generos']

    def mostrar_generos(self, obj):
        return ", ".join([genero.nombre for genero in obj.generos.all()])

    mostrar_generos.short_description = 'Géneros'

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'mostrar_artistas', 'lanzamiento', 'mostrar_generos']

    def mostrar_generos(self, obj):
        return ", ".join([genero.nombre for genero in obj.generos.all()])

    mostrar_generos.short_description = 'Géneros'

    def mostrar_artistas(self, obj):
        return ", ".join([artista.nombre for artista in obj.artistas.all()])

    mostrar_artistas.short_description = 'Artistas'

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'album', 'duracion', 'mostrar_artistas', 'mostrar_generos']

    def mostrar_generos(self, obj):
        return ", ".join([genero.nombre for genero in obj.generos.all()])

    mostrar_generos.short_description = 'Géneros'

    def mostrar_artistas(self, obj):
        return ", ".join([artista.nombre for artista in obj.artistas.all()])

    mostrar_artistas.short_description = 'Artistas'