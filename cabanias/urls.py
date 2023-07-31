from django.urls import path

from . import views


urlpatterns = [
    path('Cabanias/', views.ixCabanias.as_view(), name='cabanias'),
    path('filter/', views.CabaniaFilterView.as_view(), name='filter_cabania'),
    path('create/', views.CabaniaCreateView.as_view(), name='create_cabania'),
    path('update/<int:pk>', views.CabaniaUpdateView.as_view(), name='update_cabanias'),
    path('read/<int:pk>', views.CabaniaReadView.as_view(), name='read_cabania'),
    path('delete/<int:pk>', views.CabaniaDeleteView.as_view(), name='delete_cabania'),
    path('Cabania/', views.Cabanias, name='Cabania'),
 
]