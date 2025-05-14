from django.shortcuts import render
from .forms import ReservationForm
from .models import Reservation

def home(request):
    form = ReservationForm()
    reservations = None

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            instance = form.save()  # salva no banco de dados
            reservations = [instance]  # exibe apenas essa reserva salva
            return render(request, 'index.html', {
                'form': ReservationForm(),  # form limpo para nova entrada
                'reservations': reservations,
                'success_message': 'Reserva realizada com sucesso!'
            })

    return render(request, 'index.html', {
        'form': form,
        'reservations': reservations
    })
