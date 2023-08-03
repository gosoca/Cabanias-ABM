from django.urls import path

from . import views


urlpatterns = [
    path('', views.ixClientes.as_view(), name='clientes'),
    path('filter/', views.ClienteFilterView.as_view(), name='filter_cliente'),
    path('create/', views.ClienteCreateView.as_view(), name='create_cliente'),
    path('update/<int:pk>', views.ClienteUpdateView.as_view(), name='update_cliente'),
    path('read/<int:pk>', views.ClienteReadView.as_view(), name='read_cliente'),
    path('delete/<int:pk>', views.ClienteDeleteView.as_view(), name='delete_cliente'),
    path('cliente/', views.clientes, name='cliente'),
 
]