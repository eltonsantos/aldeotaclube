from django.urls import path
from .views import atletas

urlpatterns = [
    path('', atletas, name='atletas'),
]