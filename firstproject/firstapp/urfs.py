from django import path
from . import views

urlpatterns = [
    path('function', views.hello_World)
    path('class', views.HelloEthiopia.as_view()),
]