from django.shortcuts import render
from .forms import ReservationForm, CPFSearchForm
from .models import Reservation


def home(request):
    form = ReservationForm()
    search_form = CPFSearchForm()
    reservations = None
    success_message = None

    if request.method == 'POST':
        if 'save_reservation' in request.POST:
            form = ReservationForm(request.POST)
            if form.is_valid():
                instance = form.save()
                reservations = [instance]
                success_message = 'Reserva realizada com sucesso!'
                form = ReservationForm()  # limpa o formulário após salvar

        elif 'search_cpf' in request.POST:
            search_form = CPFSearchForm(request.POST)
            if search_form.is_valid():
                cpf = search_form.cleaned_data['cpf']
                reservations = Reservation.objects.filter(cpf=cpf)
                if not reservations:
                    success_message = 'Nenhuma reserva encontrada para o CPF informado.'
                search_form = CPFSearchForm()  # limpa o campo de busca

    return render(request, 'index.html', {
        'form': form,
        'search_form': search_form,
        'reservations': reservations,
        'success_message': success_message,
    })


def search_reservation_by_cpf(request):
    result = None
    if request.method == 'POST':
        form = CPFSearchForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            result = Reservation.objects.filter(cpf=cpf)
    else:
        form = CPFSearchForm()

    return render(request, 'search_reservation.html', {'form': form, 'result': result})
