from django.urls import path
from .views import artilharia

urlpatterns = [
    path('', artilharia, name='artilharia'),
]