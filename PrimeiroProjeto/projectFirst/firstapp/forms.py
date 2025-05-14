from django import forms
from django.utils.translation import gettext_lazy as _
from .models import MenuItem, Reservation

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'description']
        labels = {
            'name': _('Nome'),
            'price': _('Preço'),
            'description': _('Descrição'),
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email', 'contact', 'guest_count', 'comments']
        labels = {
            'first_name': _('Nome'),
            'last_name': _('Sobrenome'),
            'email': _('E-mail'),
            'contact': _('Contato'),
            'guest_count': _('Número de Convidados'),
            'comments': _('Comentários'),
        }
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 4}),
        }
