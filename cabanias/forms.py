from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from .models import Cabanias


class CabaniaFilterForm(BSModalForm):
 #   type = forms.ChoiceField(choices=Cabanias.nombre)

    class Meta:
        fields = ['type']


class CabaniaModelForm(BSModalModelForm):
    A_nacim = forms.DateField(
        error_messages={'invalid': 'Enter a valid date in YYYY-MM-DD format.'}
    )

    class Meta:
        model = Cabanias
        fields = '__all__'


