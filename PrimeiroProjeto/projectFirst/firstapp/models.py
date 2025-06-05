from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date, timedelta # Adicionado timedelta para futuras lógicas de tempo, se necessário

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    # Recomendo usar DecimalField para preços para maior precisão monetária
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.IntegerField() # Mantido IntegerField como no seu código original
    description = models.TextField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # IMPORTANTE: Removido unique=True. Isso permite que o mesmo CPF faça múltiplas reservas.
    # Se você quiser que um CPF possa fazer APENAS UMA reserva em todo o sistema, adicione unique=True novamente.
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    guest_count = models.IntegerField()
    reservation_date = models.DateField()
    comments = models.TextField(max_length=1000, blank=True)

    def clean(self):
        # Validação personalizada para limite de pessoas por dia na reserva
        max_people_per_day = 30
        
        # Filtra reservas para a mesma data, excluindo a própria reserva (para edições)
        # e soma o número de convidados.
        total_guests_for_date = Reservation.objects.filter(
            reservation_date=self.reservation_date
        ).exclude(pk=self.pk).aggregate(
            models.Sum('guest_count')
        )['guest_count__sum'] or 0 # 'or 0' garante que o total é 0 se não houver outras reservas

        # Se a adição da nova reserva exceder o limite de pessoas por dia
        if total_guests_for_date + self.guest_count > max_people_per_day:
            raise ValidationError(
                _("Limite de %s pessoas atingido para a data %s. Por favor, escolha outra data ou reduza o número de convidados.") % (max_people_per_day, self.reservation_date.strftime('%d/%m/%Y')),
                code='limit_exceeded_date' # Código de erro personalizado
            )

        # Você pode adicionar validação de CPF aqui também, se desejar uma segunda camada
        # Além da validação no forms.py
        # from .forms import validate_cpf # Importe a função de validação, se for usá-la aqui
        # try:
        #     validate_cpf(self.cpf)
        # except ValidationError as e:
        #     raise ValidationError({'cpf': e.message}) # Atribui o erro ao campo 'cpf'


    def __str__(self):
        # Melhor representação do objeto no Django Admin
        return f"Reserva de {self.first_name} {self.last_name} ({self.cpf}) em {self.reservation_date.strftime('%d/%m/%Y')}"


class CPFStatus(models.Model):
    STATUS_CHOICES = [
        ('novo', 'Novo'),
        ('limitado', 'Limitado (2 reservas / 15 dias)'),
        ('livre', 'Livre (Reservas ilimitadas)'),
        ('bloqueado', 'Bloqueado (1 por semana)'),
        ('inativo', 'Inativo'),
    ]

    # CPF é único aqui, pois este modelo gerencia o status ÚNICO de cada CPF no sistema.
    cpf = models.CharField(max_length=14, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='novo')
    ultima_reserva = models.DateField(null=True, blank=True)
    data_bloqueio = models.DateField(null=True, blank=True) # Data a partir da qual o CPF está bloqueado
    data_desbloqueio = models.DateField(null=True, blank=True) # Data em que o bloqueio termina

    def __str__(self):
        # Representação do objeto no Django Admin
        return f"{self.cpf} - {self.get_status_display()}" # get_status_display() mostra o valor legível do choice

    # --- Métodos de Conveniência usados no views.py ---

    def is_blocked(self):
        """
        Verifica se o CPF está atualmente bloqueado.
        Retorna True se o status for 'bloqueado' e a data de desbloqueio ainda não chegou.
        """
        return self.status == 'bloqueado' and self.data_desbloqueio and date.today() < self.data_desbloqueio

    def update_last_reservation_date(self, reservation_date):
        """
        Atualiza a data da última reserva para o CPF.
        Também contém a lógica para atualizar o status de 'novo' para 'livre' após a primeira reserva.
        """
        # A data da última reserva só é atualizada se for mais recente
        if not self.ultima_reserva or reservation_date > self.ultima_reserva:
            self.ultima_reserva = reservation_date
            
            # Lógica para mudar o status de 'novo' para 'livre' após a primeira reserva
            # Esta lógica considera que 'novo' é o status inicial e que uma reserva já o torna 'livre'
            if self.status == 'novo':
                self.status = 'livre'
            
            self.save() # Salva as alterações no banco de dados

    # Você pode adicionar mais métodos aqui para a lógica de 'limitado' ou outras regras:
    # def check_limited_status(self):
    #     """
    #     Verifica e ajusta o status 'limitado' com base no histórico de reservas.
    #     Isso pode ser chamado por um signal, uma tarefa agendada, ou na view.
    #     """
    #     if self.status == 'limitado':
    #         # Lógica mais complexa para decidir se o status 'limitado' deve ser alterado
    #         # Ex: contar reservas nos últimos 15 dias.
    #         pass
    #     self.save() # Salva o status atualizado