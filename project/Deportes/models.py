from django.db import models


class Equipo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del equipo")
    
    def __str__(self) -> str:
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del jugador")
    jugador = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Equipo")

    def __str__(self) -> str:
        return self.nombre
        
    class Meta:
        verbose_name_plural = "jugadores"

class Entrenador(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del entrenador")
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Entrenadores"
    
class Deporte(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del deporte")
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True, blank=True)
    jugador = models.ManyToManyField(Jugador)
    
    def __str__(self) -> str:
        return self.nombre

    


    