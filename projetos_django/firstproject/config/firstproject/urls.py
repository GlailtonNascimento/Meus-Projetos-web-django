from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstapp.urls')),  # tudo vem das rotas do app
]


