from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    guest_count = models.IntegerField()
    reservation_date = models.DateField()
    comments = models.TextField(max_length=1000, blank=True)

    def clean(self):
        max_people_per_day = 30
        total = Reservation.objects.filter(
            reservation_date=self.reservation_date
        ).exclude(pk=self.pk).aggregate(
            models.Sum('guest_count')
        )['guest_count__sum'] or 0

        if total + self.guest_count > max_people_per_day:
            raise ValidationError(
                _(f"Limite de {max_people_per_day} pessoas, atingido para essa data. {self.reservation_date}.")
            )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CPFStatus(models.Model):
    STATUS_CHOICES = [
        ('novo', 'Novo'),
        ('limitado', 'Limitado (2 reservas / 15 dias)'),
        ('livre', 'Livre (Reservas ilimitadas)'),
        ('bloqueado', 'Bloqueado (1 por semana)'),
        ('inativo', 'Inativo'),
    ]

    cpf = models.CharField(max_length=14, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='novo')
    ultima_reserva = models.DateField(null=True, blank=True)
    data_bloqueio = models.DateField(null=True, blank=True)
    data_desbloqueio = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.cpf} - {self.status}"
