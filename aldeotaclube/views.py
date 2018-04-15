from django.shortcuts import render, redirect

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')