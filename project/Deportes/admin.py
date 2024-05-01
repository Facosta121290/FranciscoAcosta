from django.contrib import admin
from . import models


admin.site.register(models.Equipo)
admin.site.register(models.Jugador)
admin.site.register(models.Entrenador)
admin.site.register(models.Deporte)