from django.urls import path
from . import views

urlpatterns = [
    path('function/', views.hello_World, name='hello_world'),
    path('class/', views.HelloEthiopia.as_view(), name='hello_ethiopia'),
    path('reservation/', views.reservation, name='reservation'),  # ADICIONE ESTA LINHA!
]