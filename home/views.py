from django.shortcuts import render, redirect
from jogos.models import Jogo
from noticias.models import Noticia

def home(request):
    jogos = Jogo.objects.order_by('-data')[:1]
    noticias = Noticia.objects.order_by('-data')[:3]
    return render(request, 'home.html', {'jogos' : jogos, 'noticias' : noticias})