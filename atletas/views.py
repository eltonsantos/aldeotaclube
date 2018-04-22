from django.shortcuts import render, redirect
from .models import Atletas

def atletas(request):
    atletas = Atletas.objects.all()
    return render(request, 'atletas.html', {'atletas' : atletas})