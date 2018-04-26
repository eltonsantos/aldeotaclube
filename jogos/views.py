from django.shortcuts import render, redirect
from .models import Jogo

def jogos(request):
    jogos = Jogo.objects.all()[:1]
    return render(request, 'jogos.html', {'jogos' : jogos})