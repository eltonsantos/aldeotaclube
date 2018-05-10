from django.urls import path
from .views import atletas, detalhes

app_name = 'atletas'

urlpatterns = [
    path('', atletas, name='atletas'),
    path('<slug:slug>', detalhes, name='detalhes'),
]