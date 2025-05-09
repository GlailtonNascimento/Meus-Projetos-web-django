from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)  # Nome do item
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do item, com casas decimais

    def __str__(self):
        return self.name


class Reservation(models.Model):
    first_name = models.CharField(max_length=255)  # Nome do cliente
    last_name = models.CharField(max_length=255)  # Sobrenome do cliente
    guest_count = models.IntegerField()  # Número de convidados
    reservation_date = models.DateTimeField()  # Data e hora da reserva
    comments = models.CharField(max_length=1000, blank=True)  # Comentários adicionais
    email = models.EmailField(max_length=255, default='email@example.com')


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_date}"