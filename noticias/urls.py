from django.urls import path
from .views import noticias

app_name = 'noticias'

urlpatterns = [
    path('', noticias, name='noticias'),
]