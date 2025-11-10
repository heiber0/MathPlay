from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from login.views import MATERIAS 

@login_required
def conceptos(request):
    return render(request, 'integrales/conceptos.html', {'materias': MATERIAS})

@login_required
def propiedades(request):
    return render(request, 'integrales/propiedades.html', {'materias': MATERIAS})

@login_required
def aplicaciones(request):
    return render(request, 'integrales/aplicaciones.html', {'materias': MATERIAS})

@login_required
def juego1(request):
    return render(request, 'integrales/juego1.html', {'materias': MATERIAS})

@login_required
def juego2(request):
    return render(request, 'integrales/juego2.html', {'materias': MATERIAS})