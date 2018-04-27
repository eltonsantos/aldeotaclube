from django.shortcuts import render, redirect
from jogos.models import Jogo

def home(request):
    jogos = Jogo.objects.order_by('-data')[:1]
    return render(request, 'home.html', {'jogos' : jogos})