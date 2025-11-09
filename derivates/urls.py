from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='derivates_home'),
    path('limites/', views.limites, name='derivates_limites'),
    path('definidas/', views.definidas, name='derivates_definidas'),
]
