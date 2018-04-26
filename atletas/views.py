from django.shortcuts import render, redirect
from .models import Atleta
from jogos.models import Jogo


def atletas(request):
    atletas = Atleta.objects.all()
    jogos = Jogo.objects.all()[:1]
    return render(request, 'atletas.html', {'atletas' : atletas, 'jogos' : jogos})