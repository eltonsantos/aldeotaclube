from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .forms import ContactForm

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    form = ContactForm(request.POST)
        
    return render(request, 'contato.html', {'form' : form})