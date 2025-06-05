from django.contrib import admin
from .models import Reservation
from .forms import ReservationForm  # Importa o formulário personalizado

class ReservationAdmin(admin.ModelAdmin):
    form = ReservationForm  # Diz ao admin para usar seu form personalizado

admin.site.register(Reservation, ReservationAdmin)
