from django.shortcuts import render, redirect

def atletas(request):
    return render(request, 'atletas.html')