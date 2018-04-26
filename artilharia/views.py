from django.shortcuts import render, redirect
from jogos.models import Jogo

def artilharia(request):
    jogos = Jogo.objects.all()[:1]
    return render(request, 'artilharia.html', {'jogos' : jogos})