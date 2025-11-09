from django.shortcuts import render

def index(request):
    return render(request, 'derivates/index.html', {'materias': []})

def limites(request):
    return render(request, 'derivates/limites.html', {'materias': []})

def definidas(request):
    return render(request, 'derivates/definidas.html')