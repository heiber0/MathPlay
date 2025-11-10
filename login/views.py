from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.

# --- Datos Simulados de Materias ---
MATERIAS = [
    {'id': 'Integrales', 'nombre': 'Integrales 📚', 'activities': [
        'Conceptos Claves de Integrales', 
        'Propiedades de Integrales', 
        'Aplicaciones de Integrales', 
        'Actividad 1: Adivina el área bajo la curva',
        'Actividad 2: Empareja la función con su integral'],
        'link': ['integrales/conceptos', 'integrales/propiedades', 'integrales/aplicaciones', 'integrales/juego1', 'integrales/juego2'],
    },
]
# --- Fin Datos Simulados ---

def materia_detail(request, materia_id):
    """Vista para mostrar las actividades de una materia seleccionada."""
    
    # Buscar la materia por ID
    materia_encontrada = next((m for m in MATERIAS if m['id'] == materia_id), None)
    
    if materia_encontrada:
        return render(request, 'materia_detail.html', {
            'materia': materia_encontrada,
            'materias': MATERIAS # Siempre pasar la lista completa para el sidebar
        })
    else:
        # Manejar error 404 o redirigir
        return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'materias': MATERIAS,
            'form': CustomUserCreationForm # USAR EL FORMULARIO PERSONALIZADO
        })
    else:
        # Aquí puedes usar el formulario para validar en lugar de request.POST['password1']
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
             # Si falla la validación del formulario (ej. usuario ya existe, contraseñas no coinciden)
            return render(request, 'signup.html', {
                'materias': MATERIAS,
                'form': form, # Pasar el formulario con los errores
                'error': form.errors # Mostrar errores de validación
            })


def home(request):
    return render(request, 'home.html', {
        'materias': MATERIAS
    })

@login_required
def task(request):
    return render(request, 'task.html', {
        'materias': MATERIAS})

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'materias': MATERIAS,
            'form': CustomAuthenticationForm # USAR EL FORMULARIO PERSONALIZADO
        })
    else:
        # En el POST, usaremos el formulario para validar credenciales.
        form = CustomAuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            # El formulario ya autenticó al usuario
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            # Si la autenticación falla (usuario/contraseña incorrectos)
            return render(request, 'signin.html', {
                'materias': MATERIAS,
                'form': form, # Pasar el formulario con errores
                'error': 'Usuario o contraseña incorrectos'
            })
