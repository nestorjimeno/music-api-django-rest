from django.test import TestCase
from .models import GeneroMusical, Artista, Album, Cancion

from datetime import timedelta

class ModelosTestCase(TestCase):

    def setUp(self):
        self.genero_rock = GeneroMusical.objects.create(nombre='Rock')
        self.artista = Artista.objects.create(nombre='Artista de Prueba', biografia='Biografía del artista')
        self.album = Album.objects.create(titulo='Álbum de Prueba', lanzamiento=2023)
        self.cancion = Cancion.objects.create(titulo='Canción de Prueba', duracion=timedelta(seconds=356), album=self.album)

        self.artista.generos.add(self.genero_rock)
        self.album.artistas.add(self.artista)
        self.album.generos.add(self.genero_rock)
        self.cancion.artistas.add(self.artista)
        self.cancion.generos.add(self.genero_rock)

    def test_creacion_modelos(self):
        genero = GeneroMusical.objects.get(nombre='Rock')
        self.assertEqual(genero.nombre, 'Rock')

        artista = Artista.objects.get(nombre='Artista de Prueba')
        self.assertEqual(artista.biografia, 'Biografía del artista')

        album = Album.objects.get(titulo='Álbum de Prueba')
        self.assertEqual(album.lanzamiento, 2023)

        cancion = Cancion.objects.get(titulo='Canción de Prueba')
        self.assertEqual(cancion.duracion, timedelta(seconds=356))

    def test_relaciones_many_to_many(self):
        artista = Artista.objects.get(nombre='Artista de Prueba')
        self.assertIn(self.genero_rock, artista.generos.all())

        album = Album.objects.get(titulo='Álbum de Prueba')
        self.assertIn(self.artista, album.artistas.all())
        self.assertIn(self.genero_rock, album.generos.all())

        cancion = Cancion.objects.get(titulo='Canción de Prueba')
        self.assertIn(self.artista, cancion.artistas.all())
        self.assertIn(self.genero_rock, cancion.generos.all())
