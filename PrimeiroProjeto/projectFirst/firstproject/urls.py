# projectFirst/firstproject/urls.py
from django.contrib import admin
from django.urls import path, include 



urlpatterns = [
    path('admin/', admin.site.urls),
    # ESTA LINHA ESTÁ CORRETA E É ESSENCIAL:
    path('', include('firstapp.urls')), 
    # REMOVA OU COMENTE ESTA LINHA:
    # path("home", views.home, name="home_raiz"), 
]