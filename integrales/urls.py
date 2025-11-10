from django.urls import path
from . import views 

urlpatterns = [
    path('conceptos/', views.conceptos, name='conceptos'),
    path('propiedades/', views.propiedades, name='propiedades'),
    path('aplicaciones/', views.aplicaciones, name='aplicaciones'), 
    path('juego1/', views.juego1, name='juego1'),
    path('juego2/', views.juego2, name='juego2'),    
]