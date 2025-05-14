from django.db import models

class MenuItem(models.Model):
    """
    Modelo para representar um item de menu.
    """
    name = models.CharField(max_length=255)         # Nome do item
    price = models.IntegerField()                   # Preço do item
    description = models.TextField()                # Descrição do item

    def __str__(self):
        return self.name


class Reservation(models.Model):
    """
    Modelo para representar uma reserva.
    """
    first_name = models.CharField(max_length=255)       # Nome do cliente
    last_name = models.CharField(max_length=255)        # Sobrenome do cliente
    email = models.EmailField()                         # Email do cliente
    contact = models.CharField(max_length=20)           # Telefone de contato
    guest_count = models.IntegerField()                 # Número de convidados
    reservation_time = models.DateTimeField(auto_now=True)  # Atualiza automaticamente a cada salvamento
    comments = models.TextField(max_length=1000, blank=True)  # Comentários adicionais (opcional)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    