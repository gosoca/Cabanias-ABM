from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from .models import Clientes


class ClienteFilterForm(BSModalForm):
    type = forms.ChoiceField(choices=Clientes.GENERO_CLIENTE)

    class Meta:
        fields = ['type']


class ClienteModelForm(BSModalModelForm):
    A_nacim = forms.DateField(
        error_messages={'invalid': 'Enter a valid date in YYYY-MM-DD format.'}
    )

    class Meta:
        model = Clientes
        fields = '__all__'


