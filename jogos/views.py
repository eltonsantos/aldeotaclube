from django.shortcuts import render, redirect
from .models import Jogos

def jogos(request):
    jogos = Jogos.objects.all()[:1]
    return render(request, 'jogos.html', {'jogos' : jogos})