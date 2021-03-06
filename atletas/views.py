from django.shortcuts import render, redirect
from .models import Atleta
from jogos.models import Jogo

def atletas(request):
    atletas = Atleta.objects.all()
    jogos = Jogo.objects.order_by('-data')[:1]
    return render(request, 'atletas.html', {'atletas' : atletas, 'jogos' : jogos})

def detalhes(request, slug):
    atleta = Atleta.objects.get(slug=slug)
    jogos = Jogo.objects.order_by('-data')[:1]
    return render(request, 'detalhe_atleta.html', {'atleta' : atleta, 'jogos' : jogos})