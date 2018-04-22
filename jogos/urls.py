from django.urls import path
from .views import jogos

urlpatterns = [
    path('', jogos, name='jogos'),
]