from django.urls import path
from .views import noticias, detalhes

app_name = 'noticias'

urlpatterns = [
    path('', noticias, name='noticias'),
    path('<slug:slug>', detalhes, name='detalhes'),
]