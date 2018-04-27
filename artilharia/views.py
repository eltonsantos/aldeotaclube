from django.shortcuts import render, redirect
from jogos.models import Jogo

def artilharia(request):
    jogos = Jogo.objects.order_by('-data')[:1]
    return render(request, 'artilharia.html', {'jogos' : jogos})