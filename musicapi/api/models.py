from django.db import models

class GeneroMusical(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Artista(models.Model):
    nombre = models.CharField(max_length=200)
    genero = models.ForeignKey(GeneroMusical, on_delete=models.CASCADE)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=200)
    lanzamiento = models.IntegerField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    genero = models.ForeignKey(GeneroMusical, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    duracion = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo