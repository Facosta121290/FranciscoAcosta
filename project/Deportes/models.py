from django.db import models


class Deporte(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=200)
    deporte = models.ForeignKey(Deporte, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

class Entrenador(models.Model):
    nombre = models.CharField(max_length=200)
    deporte = models.ForeignKey(Deporte, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre