from django.shortcuts import render
from .forms import ReservationForm

def hello_World(request):
    return HttpResponse("Hello World!")

def home(request):
    form = ReservationForm()  # Inicializa o formulário vazio
    reservation_success = False  # Variável para controle de sucesso
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Aqui você pode processar os dados do formulário, por exemplo, salvar no banco de dados
            form.save()  # Salvar a reserva no banco de dados
            reservation_success = True  # Indica que a reserva foi realizada com sucesso
            form = ReservationForm()  # Reseta o formulário para um novo preenchimento

    return render(request, 'index.html', {'form': form, 'reservation_success': reservation_success})


   