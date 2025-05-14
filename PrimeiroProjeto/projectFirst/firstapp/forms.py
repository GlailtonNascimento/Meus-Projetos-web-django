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
        fields = ['first_name', 'last_name','cpf','email', 'contact', 'guest_count', 'reservation_date', 'comments']
        labels = {
            'first_name': _('Nome'),
            'last_name': _('Sobrenome'),
            'cpf': _('CPF'),
            'email': _('E-mail'),
            'contact': _('Contato'),
            'guest_count': _('Número de Convidados'),
            'reservation_date': _('Data da Reserva'),
            'comments': _('Comentários'),
        }
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'comments': forms.Textarea(attrs={'rows': 4}),
        }

        

class CPFSearchForm(forms.Form):
    cpf = forms.CharField(
        label=_("CPF"),
        max_length=14,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu CPF'})
    )


