from django.urls import path
from . import views 

app_name = "Deportes"

urlpatterns = [
    path("", views.home, name='home'),
]