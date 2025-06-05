# firstapp/urls.py
from django.urls import path
from . import views #  o '.views'  está no mesmo diretório do app

urlpatterns = [
    # Mapeia a URL raiz do aplicativo (ex: http://127.0.0.1:8000/) para a view 'home'
    path('', views.home, name='home'), 

    # Se tiver outras views no  'firstapp/views.py' no projeto,
    # você as adicionaria aqui. Por exemplo:
    # path('contato/', views.contact_page, name='contact'),
    # path('sobre/', views.about_page, name='about'),
]