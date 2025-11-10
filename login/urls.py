from django.contrib import admin
from django.urls import path, include
import login.views as login_views

urlpatterns = [
    path('', login_views.home,name='home'),
    path('signup/', login_views.signup, name='signup'),
    path('task/', login_views.task, name='task'),
    path('logout/', login_views.signout, name='logout'),
    path('signin/', login_views.signin, name='signin'),
    # NUEVA RUTA: Para cargar los detalles de la materia (e.g., /materia/algebra/)
    path('materia/<str:materia_id>/', login_views.materia_detail, name='materia_detail'),
]