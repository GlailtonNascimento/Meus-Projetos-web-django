# firstapp/forms.py

import re
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.conf import settings # Importe as configurações do Django

# LINHA PARA DEBUG: Verifique o valor de DEBUG no console ao iniciar o servidor
print(f"DEBUG está definido como: {settings.DEBUG}")

from .models import MenuItem, Reservation, CPFStatus 

# --- FUNÇÃO DE VALIDAÇÃO DE CPF (CONDICIONAL: TESTE vs. PRODUÇÃO) ---
def validate_cpf(value):
    # Remove caracteres não numéricos ANTES de qualquer validação.
    # O valor retornado por esta função será o CPF LIMPO.
    cpf_cleaned = re.sub(r'[^0-9]', '', value) 

    # --- LÓGICA DE VALIDAÇÃO CONDICIONAL ---
    if settings.DEBUG:
        # Se DEBUG for True (ambiente de desenvolvimento/teste)
        # Permite qualquer sequência de 11 dígitos para testes
        if len(cpf_cleaned) != 11:
            raise ValidationError(_('CPF de teste deve conter 11 dígitos numéricos.'), code='invalid_test_length')
        
        # Opcional: Adicione outras regras mínimas para testes se desejar, por exemplo, não permitir vazio
        if not cpf_cleaned.strip():
            raise ValidationError(_('CPF de teste não pode ser vazio.'), code='empty_test_cpf')

        return cpf_cleaned # Retorna o CPF limpo para testes
    
    else:
        # Se DEBUG for False (ambiente de produção)
        # Aplica a validação completa do CPF
        if len(cpf_cleaned) != 11:
            raise ValidationError(_('CPF deve conter 11 dígitos numéricos.'), code='invalid_length')

        # Verifica CPFs com todos os dígitos iguais (ex: "11111111111")
        if cpf_cleaned in [s * 11 for s in [str(i) for i in range(10)]]:
            raise ValidationError(_('CPF inválido.'), code='invalid_sequence')

        # Validação do primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf_cleaned[i]) * (10 - i)
        resto = 11 - (soma % 11)
        digito1 = 0 if resto > 9 else resto

        if digito1 != int(cpf_cleaned[9]):
            raise ValidationError(_('CPF inválido.'), code='invalid_first_digit')

        # Validação do segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf_cleaned[i]) * (11 - i)
        resto = 11 - (soma % 11)
        digito2 = 0 if resto > 9 else resto

        if digito2 != int(cpf_cleaned[10]):
            raise ValidationError(_('CPF inválido.'), code='invalid_second_digit')

        return cpf_cleaned # Retorna o CPF limpo validado para produção

# --- FIM DA FUNÇÃO DE VALIDAÇÃO DE CPF ---


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
    # SOBRESCREVER O CAMPO CPF AQUI PARA ADICIONAR O WIDGET E HELP_TEXT
    cpf = forms.CharField(
        max_length=14, # Permite que o usuário digite com pontos e hífens
        label=_('CPF'), # Define o label para o campo
        help_text=_("Insira apenas números (11 dígitos). Pontos e hífens serão ignorados."), # Dica para o usuário
        widget=forms.TextInput(attrs={'placeholder': '12345678900'}), # O placeholder desejado
        validators=[validate_cpf] # Aplica a validação CONDICIONAL aqui
    )

    class Meta:
        model = Reservation
        # Inclua todos os campos, mas a definição de 'cpf' acima irá sobrescrever
        fields = ['first_name', 'last_name','cpf','email', 'contact', 'guest_count', 'reservation_date', 'comments'] 
        labels = {
            'first_name': _('Nome'),
            'last_name': _('Sobrenome'),
            # 'cpf': _('CPF'), 
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

    # O método clean_cpf é chamado DEPOIS que os validadores (como validate_cpf) são executados.
    # Como validate_cpf já retorna o CPF limpo, aqui apenas pegamos esse valor.
    def clean_cpf(self):
        # O self.cleaned_data['cpf'] já conterá o CPF limpo (apenas números)
        # porque validate_cpf o processou e o retornou.
        cpf = self.cleaned_data['cpf']
        return cpf # Retorna o CPF LIMPO

class CPFSearchForm(forms.Form):
    # ATUALIZADO O CAMPO CPF PARA TER O PLACEHOLDER E HELP_TEXT DESEJADOS
    cpf = forms.CharField(
        label=_("CPF"),
        max_length=14, # Manter max_length para permitir formatação (ex: 123.456.789-00)
        help_text=_("Insira apenas números (11 dígitos)."), # Dica para o usuário
        widget=forms.TextInput(attrs={'placeholder': '12345678900'}), # O placeholder desejado
        validators=[validate_cpf] # Aplica a validação CONDICIONAL aqui
    )

    # Não precisamos de um clean_cpf aqui se validate_cpf já faz o trabalho de limpeza e validação.
    # O valor em self.cleaned_data['cpf'] já virá limpo da função validate_cpf.