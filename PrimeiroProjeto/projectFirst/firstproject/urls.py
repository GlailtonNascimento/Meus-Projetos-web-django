"""
Configuração de URLs para o projeto firstproject.

Mais informações: https://docs.djangoproject.com/pt-br/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('firstapp.urls')),  # Inclui as URLs da aplicação 'firstapp'
]
