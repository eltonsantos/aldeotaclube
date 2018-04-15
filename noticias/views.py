from django.shortcuts import render, redirect

def noticias(request):
    return render(request, 'noticias.html')