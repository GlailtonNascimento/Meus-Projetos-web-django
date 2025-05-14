from django.urls import path
from . import views

urlpatterns = [
    path('function/', views.hello_world),          # URL para view baseada em função
    path('class/', views.HelloEthiopia.as_view()), # URL para view baseada em classe
]
