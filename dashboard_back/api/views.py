import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .facade import format_moeda, format_populacao

def get_qtd_municipios(estado_sigla, data_municipios):
  quantidade_municipios = 0
  for municipio in data_municipios:
    sigla_municipio = municipio['microrregiao']['mesorregiao']['UF']['sigla']
    if sigla_municipio == estado_sigla:
      quantidade_municipios += 1
  return quantidade_municipios

def get_populacao(estado_id):
    url_populacao = f'https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N3[{estado_id}]'
    response = requests.get(url_populacao)
    if response.status_code == 200:
        data = response.json()
        populacao = data[0]['resultados'][0]['series'][0]['serie']['2021']
        return populacao
    else:
        return 0
    
def get_pib(estado_id):
    url_pib = f'https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/2021/variaveis/37?localidades=N3[{estado_id}]'
    response = requests.get(url_pib)
    if response.status_code == 200:
        data = response.json()
        pib = data[0]['resultados'][0]['series'][0]['serie']['2021']
        return pib 
    else:
        return 0
    
def get_rendimento_mensal(estado_id):
    url_rendimento_mensal = f'https://servicodados.ibge.gov.br/api/v3/agregados/4660/periodos/2023/variaveis/5933?localidades=N3[{estado_id}]'
    response = requests.get(url_rendimento_mensal)
    if response.status_code == 200:
        data = response.json()
        rendimento_mensal = data[0]['resultados'][0]['series'][0]['serie']['2023']
        return rendimento_mensal
    else:
        return 0
class EstadoDetailView(APIView):
    def get(self, request, estado_sigla):
        url_municipios = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
        response_municipios = requests.get(url_municipios)
        data_municipios = response_municipios.json()
        
        estado_info_map = {}
        for municipio in data_municipios:
            sigla = municipio['microrregiao']['mesorregiao']['UF']['sigla']
            estado_id = municipio['microrregiao']['mesorregiao']['UF']['id']
            estado_nome = municipio['microrregiao']['mesorregiao']['UF']['nome']
            estado_info_map[sigla] = {'id': estado_id, 'nome': estado_nome}

        if estado_sigla not in estado_info_map:
            return Response({"error": "Estado não encontrado"}, status=404)
        
        estado_info = estado_info_map[estado_sigla]
        estado_id = estado_info['id']
        estado_nome = estado_info['nome']
        quantidade_municipios = get_qtd_municipios(estado_sigla, data_municipios)
        populacao = get_populacao(estado_id)
        pib = get_pib(estado_id)
        rendimento_mensal = get_rendimento_mensal(estado_id)

        estado_data = {
            'id': estado_id,
            'nome': estado_nome,
            'sigla': estado_sigla,
            'quantidade_municipios': quantidade_municipios,
            'populacao': format_populacao(populacao),
            'pib': format_moeda(pib),
            'rendimento_mensal': format_moeda(rendimento_mensal),
        }
        
        
        return Response(estado_data)


class MunicipiosQtdListView(APIView):
    def get(self, request):
        url_municipios = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
        response_municipios = requests.get(url_municipios)
        data_municipios = response_municipios.json()
        
        estado_info_map = {}
        for municipio in data_municipios:
            sigla = municipio['microrregiao']['mesorregiao']['UF']['sigla']
            estado_id = municipio['microrregiao']['mesorregiao']['UF']['id']
            estado_nome = municipio['microrregiao']['mesorregiao']['UF']['nome']
            if sigla not in estado_info_map:
                estado_info_map[sigla] = {'id': estado_id, 'nome': estado_nome, 'quantidade_municipios': 1}
            else:
                estado_info_map[sigla]['quantidade_municipios'] += 1

        estados_data = []
        for sigla, estado_info in estado_info_map.items():
            estado_id = estado_info['id']
            estado_nome = estado_info['nome']
            quantidade_municipios = estado_info['quantidade_municipios']
            populacao = get_populacao(estado_id)
            pib = get_pib(estado_id)
            rendimento_mensal = get_rendimento_mensal(estado_id)

            estado_data = {
                'id': estado_id,
                'nome': estado_nome,
                'sigla': sigla,
                'quantidade_municipios': quantidade_municipios,
                'populacao': int(populacao),
                'pib': int(pib),
                'rendimento_mensal': int(rendimento_mensal),
            }
            estados_data.append(estado_data)

        return Response(estados_data)