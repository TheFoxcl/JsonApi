from django.urls import path
from .views import CelularesView

# cracion de ruta nuueva para el View
urlpatterns = [
    path('clientes/',CelularesView.as_view(),name='clientes_list'),
    path('clientes/<int:id>',CelularesView.as_view(),name='clientes_process'),
]
