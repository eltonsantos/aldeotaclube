from django.shortcuts import render, redirect
from .models import Jogo

def jogos(request):
    jogos = Jogo.objects.order_by('-data')[:1]
    lista_jogos = Jogo.objects.all()
    return render(request, 'jogos.html', {'jogos' : jogos, 'lista_jogos' : lista_jogos})