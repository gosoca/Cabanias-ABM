from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import (
    ClienteModelForm,
    ClienteFilterForm,
)

from .models import Clientes



class ixClientes(generic.ListView):
    model = Clientes
    context_object_name = 'clientes'
    template_name = 'clientes.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if 'type' in self.request.GET:
            qs = qs.filter( genero_cliente=int(self.request.GET['type']))
        return qs
    

class ClienteFilterView(BSModalFormView):
    template_name = 'examples/filter_cliente.html' 
    form_class = ClienteFilterForm
    def form_valid(self, form):
        self.filter = '?type=' + form.cleaned_data['type']
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('clientes') + self.filter

class ClienteCreateView(BSModalCreateView):
    template_name = 'examples/create_cliente.html'
    form_class = ClienteModelForm
    success_message = 'Success: Cliente dado de alta.'
    success_url = reverse_lazy('clientes')


class ClienteUpdateView(BSModalUpdateView):
    model = Clientes
    template_name = 'examples/update_cliente.html'
    form_class = ClienteModelForm
    success_message = 'Success: Cliente Actualizado.'
    success_url = reverse_lazy('clientes')

class ClienteReadView(BSModalReadView):
    model = Clientes
    template_name = 'examples/read_cliente.html'

class ClienteDeleteView(BSModalDeleteView):
    model = Clientes
    template_name = 'examples/delete_cliente.html'
    success_message = 'Success: Cliente Eliminado.'
    success_url = reverse_lazy('clientes')



def clientes(request):
    data = {}
    if request.method == 'GET':
        clientes = Clientes.objects.all()
        data['table'] = render_to_string(
            'clientes_tabla.html',
            {'clientes': clientes},
            request=request
        )
        return JsonResponse(data)