from django.urls import reverse
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_estado_detail_view(api_client):
    url = reverse('estado-detail', kwargs={'estado_sigla': 'RJ'})
    response = api_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_municipios_qtd_list_view(api_client):
    url = reverse('estados-list')
    response = api_client.get(url)
    assert response.status_code == 200
