from django.shortcuts import render

from . import models

def home(request):
    query = models.Deporte.objects.all()
    context = {"deportes": query}
    return render(request, "Deportes/index.html", context)
