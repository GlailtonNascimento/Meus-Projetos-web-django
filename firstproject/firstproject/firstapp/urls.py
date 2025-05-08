from django.urls import path
from . import views

urlpatterns = [
    path('function', views.hello_World),  # Adicionada a vírgula
    path('class', views.HelloEthiopia.as_view()),
]