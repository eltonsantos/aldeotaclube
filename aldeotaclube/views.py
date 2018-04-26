from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from jogos.models import Jogo

from .forms import ContactForm

def sobre(request):
    jogos = Jogo.objects.all()[:1]
    return render(request, 'sobre.html', {'jogos' : jogos})

def contato(request):
    form = ContactForm(request.POST)
    jogos = Jogo.objects.all()[:1]
    return render(request, 'contato.html', {'form' : form, 'jogos' : jogos})