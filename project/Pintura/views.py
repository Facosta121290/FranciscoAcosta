from django.shortcuts import render

from . import models

def home(request):
    query = models.TipoPintura.objects.all()
    context = {"pinturas": query}
    return render(request, "Pinturas/index.html", context)