import requests
from django.core.management.base import BaseCommand
from api.models import Estado, Municipio

class Command(BaseCommand):
    help = 'Load data from IBGE API'

    def handle(self, *args, **kwargs):
        # Get municipios data
        url_municipios = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
        response_municipios = requests.get(url_municipios)
        data_municipios = response_municipios.json()

        # Clear existing data
        Municipio.objects.all().delete()
        Estado.objects.all().delete()

        estado_info_map = {}
        for municipio in data_municipios:
            estado_sigla = municipio['microrregiao']['mesorregiao']['UF']['sigla']
            estado_id = municipio['microrregiao']['mesorregiao']['UF']['id']
            estado_nome = municipio['microrregiao']['mesorregiao']['UF']['nome']
            municipio_id = municipio['id']
            municipio_nome = municipio['nome']

            if estado_id not in estado_info_map:
                estado_info_map[estado_id] = {
                    'id': estado_id,
                    'nome': estado_nome,
                    'sigla': estado_sigla,
                    'municipios': []
                }

            estado_info_map[estado_id]['municipios'].append({
                'id': municipio_id,
                'nome': municipio_nome,
            })

        for estado_info in estado_info_map.values():
            estado_id = estado_info['id']
            populacao = self.get_populacao(estado_id)
            pib = self.get_pib(estado_id)
            rendimento_mensal = self.get_rendimento_mensal(estado_id)

            estado = Estado.objects.create(
                id=estado_id,
                nome=estado_info['nome'],
                sigla=estado_info['sigla'],
                populacao=populacao,
                pib=pib,
                rendimento_mensal=rendimento_mensal
            )

            for municipio_info in estado_info['municipios']:
                Municipio.objects.create(
                    id=municipio_info['id'],
                    nome=municipio_info['nome'],
                    estado=estado
                )

    def get_populacao(self, estado_id):
        url_populacao = f'https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[{estado_id}]'
        response = requests.get(url_populacao)
        if response.status_code == 200:
            data = response.json()
            return data[0]['resultados'][0]['series'][0]['serie']['2021']
        return 0

    def get_pib(self, estado_id):
        url_pib = f'https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/2021/variaveis/37?localidades=N3[{estado_id}]'
        response = requests.get(url_pib)
        if response.status_code == 200:
            data = response.json()
            return data[0]['resultados'][0]['series'][0]['serie']['2021']
        return 0

    def get_rendimento_mensal(self, estado_id):
        url_rendimento_mensal = f'https://servicodados.ibge.gov.br/api/v3/agregados/4660/periodos/2023/variaveis/5933?localidades=N3[{estado_id}]'
        response = requests.get(url_rendimento_mensal)
        if response.status_code == 200:
            data = response.json()
            return data[0]['resultados'][0]['series'][0]['serie']['2023']
        return 0