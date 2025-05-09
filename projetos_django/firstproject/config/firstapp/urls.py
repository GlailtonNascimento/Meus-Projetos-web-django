from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ponto de entrada da home (raiz do site)
    path('function/', views.hello_World),
    path('reservation/', views.home),  # Para acesso direto à página de reserva
]

