from django.urls import path
from . import views

app_name = "Pintura"

urlpatterns = [
    path("", views.home),
]