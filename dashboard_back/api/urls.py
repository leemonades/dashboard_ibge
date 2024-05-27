from django.urls import path
from .views import EstadoDetailView, EstadosListView

urlpatterns = [
    path('estado/<str:estado_sigla>/', EstadoDetailView.as_view(), name='estado-detail'),
    path('estados/', EstadosListView.as_view(), name='estados-list'),
]