from django.db import models



# Create your models here.
class MenuItem(models.Model):
    """
    Modelo para representar um item de menu.
    """
    name = models.CharField(max_length=255)  # Nome do item
    price = models.IntegerField()  # Preço do item
    description = models.TextField()  # Descrição do item

    def __str__(self):
        return self.name  # Retorna o nome do item como representação em string
