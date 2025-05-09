from django.shortcuts import render  # Para renderizar templates HTML / To render HTML templates
from django.http import HttpResponse    # Para retornar respostas HTTP simples / To return simple HTTP responses
from django.views import View          # Classe base para criar views / Base class for creating views
from .forms import ReservationForm    # Importa o formulário de reserva / Imports the reservation form

# Create your views here./# Crie suas views aqui.
def hello_World(request):
    return HttpResponse("Hello World!")

class HelloEthiopia(View):
    def get(self, request):
        return HttpResponse("Hello Ethiopia!")
    

def home(request):
    form = ReservationForm()  # Inicializa o formulário uma vez.
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data/ # Processar os dados em form.cleaned_data.
            return HttpResponse("Reservation successful!")
            
    return render(request, 'index.html', {'form': form})
   