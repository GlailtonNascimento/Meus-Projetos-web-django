from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db import transaction # Import para garantir que as operações de BD são atômicas
from datetime import date, timedelta # Import para lidar com cálculos de data (ex: 15 dias)

from .forms import ReservationForm, CPFSearchForm
from .models import Reservation, CPFStatus # Importe o modelo CPFStatus

def home(request):
    form = ReservationForm()
    search_form = CPFSearchForm()
    reservations = None

    if request.method == 'POST':
        if 'save_reservation' in request.POST:
            form = ReservationForm(request.POST)
            if form.is_valid():
                cpf = form.cleaned_data['cpf']
                reservation_date = form.cleaned_data['reservation_date']
                guest_count = form.cleaned_data['guest_count'] # Obter guest_count para a validação de limite

                # --- PRÁTICA DE NEGÓCIO: VERIFICAR CPFStatus ANTES DE SALVAR ---
                try:
                    # Tenta obter o CPFStatus existente ou cria um novo se não existir
                    cpf_status, created = CPFStatus.objects.get_or_create(cpf=cpf)

                    # 1. Verificação de Bloqueio
                    if cpf_status.status == 'bloqueado' and cpf_status.data_desbloqueio and date.today() < cpf_status.data_desbloqueio:
                        messages.error(request, f"Seu CPF está bloqueado para novas reservas até {cpf_status.data_desbloqueio.strftime('%d/%m/%Y')}. Por favor, entre em contato para mais informações.")
                        # Renderiza a página novamente com a mensagem de erro
                        return render(request, 'index.html', {'form': form, 'search_form': search_form, 'reservations': reservations})
                    
                    # 2. Verificação de Limite para Status 'limitado' (ex: 2 reservas / 15 dias)
                    if cpf_status.status == 'limitado':
                        # Conta as reservas que este CPF fez nos últimos 15 dias
                        recent_reservations_count = Reservation.objects.filter(
                            cpf=cpf,
                            reservation_date__gte=date.today() - timedelta(days=15)
                        ).count()

                        if recent_reservations_count >= 2: # Limite de 2 reservas em 15 dias
                            messages.warning(request, "Você atingiu o limite de 2 reservas nos últimos 15 dias para o seu CPF. Por favor, tente novamente mais tarde.")
                            return render(request, 'index.html', {'form': form, 'search_form': search_form, 'reservations': reservations})
                        
                except Exception as e:
                    # Captura qualquer outro erro inesperado durante a verificação do CPFStatus
                    messages.error(request, f"Ocorreu um erro ao verificar o status do CPF: {e}")
                    return render(request, 'index.html', {'form': form, 'search_form': search_form, 'reservations': reservations})
                # --- FIM DA PRÉ-VERIFICAÇÃO DE CPFStatus ---

                # Se as pré-verificações do CPFStatus passarem, tenta salvar a reserva
                try:
                    with transaction.atomic(): # Garante que as operações são atômicas (tudo ou nada)
                        # Salva a reserva (isso também acionará o método clean() do modelo Reservation)
                        instance = form.save() 

                        # --- PRÁTICA DE NEGÓCIO: ATUALIZAR CPFStatus APÓS RESERVA ---
                        # Atualiza a data da última reserva no CPFStatus
                        cpf_status.ultima_reserva = reservation_date
                        
                        # Exemplo de lógica para mudar o status de 'novo' para 'livre' após a primeira reserva
                        if cpf_status.status == 'novo' and Reservation.objects.filter(cpf=cpf).count() >= 1:
                            cpf_status.status = 'livre'
                        
                        cpf_status.save() # Salva as alterações no CPFStatus
                        # --- FIM DA ATUALIZAÇÃO DE CPFStatus ---

                    messages.success(request, 'Reserva realizada com sucesso!')
                    return redirect(reverse('home')) # Redireciona para a mesma página (PRG pattern)

                except ValidationError as e:
                    # Captura ValidationError levantado no método clean() do modelo Reservation
                    # ou por validadores de campo (como o CPF)
                    if hasattr(e, 'message_dict'):
                        for field, errors in e.message_dict.items():
                            for error in errors:
                                # Adiciona o erro ao campo específico, se for um erro de campo
                                if field != '__all__':
                                    messages.error(request, f"{form.fields[field].label}: {error}")
                                else: # Se for um erro global do formulário/modelo (ex: do clean())
                                    messages.error(request, error)
                    else: # Caso seja um ValidationError sem message_dict (menos comum para formulários)
                        messages.error(request, str(e))
                
                except Exception as e:
                    # Captura qualquer outro erro inesperado durante o processo de salvamento
                    messages.error(request, f"Ocorreu um erro inesperado ao salvar a reserva: {e}")

            # Se o formulário não for válido (form.is_valid() = False),
            # os erros do formulário serão exibidos automaticamente no template {{ form.as_p }}
            # Nenhuma mensagem de erro genérica é estritamente necessária aqui,
            # pois os erros do campo serão exibidos diretamente.
            # else:
            #    messages.error(request, 'Por favor, corrija os erros no formulário.')

        elif 'search_cpf' in request.POST:
            search_form = CPFSearchForm(request.POST)
            if search_form.is_valid():
                cpf = search_form.cleaned_data['cpf']
                reservations = Reservation.objects.filter(cpf=cpf)

                # --- PRÁTICA DE NEGÓCIO: MOSTRAR STATUS DO CPF AO BUSCAR ---
                try:
                    cpf_status = CPFStatus.objects.get(cpf=cpf)
                    messages.info(request, f"Status do CPF {cpf}: {cpf_status.get_status_display()}")
                    # Exibe avisos se o CPF estiver bloqueado/limitado
                    if cpf_status.status == 'bloqueado':
                         messages.warning(request, f"Atenção: Este CPF está bloqueado até {cpf_status.data_desbloqueio.strftime('%d/%m/%Y')}.")
                    elif cpf_status.status == 'limitado':
                         messages.warning(request, "Atenção: Este CPF está com o status 'Limitado'.")

                except CPFStatus.DoesNotExist:
                    messages.info(request, "Nenhum status de CPF encontrado para o CPF informado.")
                # --- FIM DA PRÁTICA DE NEGÓCIO ---

                if not reservations:
                    messages.info(request, 'Nenhuma reserva encontrada para o CPF informado.')
            else:
                # Se o formulário de busca não for válido (ex: CPF mal formatado)
                messages.error(request, 'O CPF informado é inválido. Por favor, corrija.')

    # Renderiza o template com os formulários, reservas e mensagens
    return render(request, 'index.html', {
        'form': form,
        'search_form': search_form,
        'reservations': reservations,
    })


# Esta view só é necessária se você tiver uma URL específica para ela.
# Se toda a funcionalidade de busca está na home, esta pode ser removida.
def search_reservation_by_cpf(request):
    result = None
    if request.method == 'POST':
        form = CPFSearchForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            result = Reservation.objects.filter(cpf=cpf)
            
            # Similar à home, você pode adicionar a lógica de exibição de status do CPF aqui
            try:
                cpf_status = CPFStatus.objects.get(cpf=cpf)
                messages.info(request, f"Status do CPF {cpf}: {cpf_status.get_status_display()}")
            except CPFStatus.DoesNotExist:
                messages.info(request, "Nenhum status de CPF encontrado para o CPF informado.")

            if not result:
                messages.info(request, 'Nenhuma reserva encontrada para o CPF informado.')
        else:
            messages.error(request, 'O CPF informado é inválido. Por favor, corrija.')
    else:
        form = CPFSearchForm()

    return render(request, 'search_reservation.html', {'form': form, 'result': result})