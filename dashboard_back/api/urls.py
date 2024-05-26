from django.urls import path
from .views import EstadoDetailView, MunicipiosQtdListView

urlpatterns = [
    path('estado/<str:estado_sigla>/', EstadoDetailView.as_view(), name='estado-detail'),
    path('estados/', MunicipiosQtdListView.as_view(), name='estados-list'),
]