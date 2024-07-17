from django.db import models

class GeneroMusical(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Artista(models.Model):
    nombre = models.CharField(max_length=200)
    generos = models.ManyToManyField(GeneroMusical)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=200)
    lanzamiento = models.IntegerField()
    artistas = models.ManyToManyField(Artista)
    generos = models.ManyToManyField(GeneroMusical)

    def __str__(self):
        return self.titulo

class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    duracion = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artistas = models.ManyToManyField(Artista)
    generos = models.ManyToManyField(GeneroMusical)

    def __str__(self):
        return self.titulo