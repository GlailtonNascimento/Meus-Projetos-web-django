from django.urls import path  # Para definir padrões de URL / To define URL patterns
from . import views  # Importa as views deste aplicativo / Imports the views from this application

urlpatterns = [
    path('function', views.hello_World),  # Mapeia a URL '/function/' para a view hello_World / Maps the URL '/function/' to the hello_World view
    path('class', views.HelloEthiopia.as_view()),  # Mapeia a URL '/class/' para a view HelloEthiopia (como view de classe) / Maps the URL '/class/' to the HelloEthiopia view (as a class-based view)
    path('reservation', views.home,),  # Mapeia a URL '/reservation/' para a view home / Maps the URL '/reservation/' to the home view
]