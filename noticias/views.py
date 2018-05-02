from django.shortcuts import render, redirect
from .models import Noticia
from jogos.models import Jogo

def noticias(request):
    noticias = Noticia.objects.all()
    jogos = Jogo.objects.order_by('-data')[:1]
    return render(request, 'noticias.html', {'noticias' : noticias, 'jogos' : jogos})
