from django.db import models

class TipoPintura(models.Model):
    """Muestra los diferentes tipos de pinturas"""
    nombre = models.CharField(max_length=200, unique=True, verbose_name="Tipo de Pintura")
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "tipos de pinturas"
        verbose_name_plural = "tipos de pinturas"

class Materiales(models.Model):
    """Es la herramienta con la que se pinta"""
    nombre = models.CharField(max_length=200, unique=True, verbose_name="Herramienta a utilizar")
    

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "tipos de herramientas"
        verbose_name_plural = "tipos de herramienta"

class Lienzos(models.Model):
    nombre = models.CharField(max_length=200, unique=True, verbose_name="Tipo de Lienzo")
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "tipo de lienzo"
        verbose_name_plural = "tipo de lienzo"

class Participante(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre pintor")
    lienzo = models.ForeignKey(Lienzos, on_delete=models.SET_NULL, null=True, blank=True)
    materiales = models.ManyToManyField(Materiales)
    
    def __str__(self) -> str:
        return self.nombre