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
    CabaniaModelForm,
    CabaniaFilterForm,
)

from .models import Cabanias



class ixCabanias(generic.ListView):
    model = Cabanias
    context_object_name = 'cabanias'
    template_name = 'cabanias.html'

#se usa en caso de tener un desplegable en el template
    """ def get_queryset(self):
        qs = super().get_queryset()
        if 'type' in self.request.GET:
            qs = qs.filter( genero_cliente=int(self.request.GET['type']))
        return qs """
    

class CabaniaFilterView(BSModalFormView):
    template_name = 'examples/filter_cabania.html' 
    form_class = CabaniaFilterForm
    def form_valid(self, form):
        self.filter = '?type=' + form.cleaned_data['type']
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('cabanias') + self.filter

class CabaniaCreateView(BSModalCreateView):
    template_name = 'examples/create_cabania.html'
    form_class = CabaniaModelForm
    success_message = 'Success: Cabaña dada de alta.'
    success_url = reverse_lazy('cabanias')


class CabaniaUpdateView(BSModalUpdateView):
    model = Cabanias
    template_name = 'examples/update_cabania.html'
    form_class = CabaniaModelForm
    success_message = 'Success: Cabaña Actualizada.'
    success_url = reverse_lazy('cabanias')

class CabaniaReadView(BSModalReadView):
    model = Cabanias
    template_name = 'examples/read_cabania.html'

class CabaniaDeleteView(BSModalDeleteView):
    model = Cabanias
    template_name = 'examples/delete_cabania.html'
    success_message = 'Success: Cabaña Eliminada.'
    success_url = reverse_lazy('cabania')



def cabanias(request):
    data = {}
    if request.method == 'GET':
        cabanias = Cabanias.objects.all()
        data['table'] = render_to_string(
            'cabanias_tabla.html',
            {'cabanias': cabanias},
            request=request
        )
        return JsonResponse(data)