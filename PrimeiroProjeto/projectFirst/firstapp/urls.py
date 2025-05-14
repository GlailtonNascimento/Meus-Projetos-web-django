from django.urls import path
from . import views

urlpatterns = [
    path('Reservation/', views.home, name='home'),  # Página principal de reservas
    #  poderei adicionar outras URLs no futuro:
    # path('Menu/', views.menu, name='menu'),
    # path('Contato/', views.contact, name='contact'),
]
