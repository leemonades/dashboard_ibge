import requests
from openpyxl import Workbook

dados_municipios = []
codigos_estados = [
    12, 27, 13, 16, 29, 23, 53, 32, 21, 52, 31, 50, 15, 25, 51, 26, 22,
    33, 24, 11, 14, 43, 41, 42, 35, 28, 17
]

url_populacao = 'https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[all]'
url_pib = 'https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/2021/variaveis/37?localidades=N6[all]'
url_rendimento_mensal = 'https://servicodados.ibge.gov.br/api/v3/agregados/4660/periodos/2023/variaveis/5933?localidades=N6[all]'

response_populacao = requests.get(url_populacao)
populacao_data = response_populacao.json()
populacao_dict = {int(item['localidade']['id']): item['serie']['2021'] for item in populacao_data[0]['resultados'][0]['series']}

response_pib = requests.get(url_pib)
pib_data = response_pib.json()
pib_dict = {int(item['localidade']['id']): item['serie']['2021'] for item in pib_data[0]['resultados'][0]['series']}

response_rendimento = requests.get(url_rendimento_mensal)
rendimento_data = response_rendimento.json()
rendimento_dict = {int(item['localidade']['id']): item['serie']['2023'] for item in rendimento_data[0]['resultados'][0]['series']}

for codigo_estado in codigos_estados:
    url_municipios = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{codigo_estado}/municipios'
    response_municipios = requests.get(url_municipios)
    municipios = response_municipios.json()

    for municipio in municipios:
        municipio_id = municipio['id']
        populacao = populacao_dict.get(municipio_id, 0)
        pib = pib_dict.get(municipio_id, 0)
        rendimento_mensal = rendimento_dict.get(municipio_id, 0)

        dados_municipios.append([
            municipio['microrregiao']['mesorregiao']['UF']['id'],
            municipio['microrregiao']['mesorregiao']['UF']['nome'],
            municipio['microrregiao']['mesorregiao']['UF']['sigla'],
            municipio['id'],
            municipio['nome'],
            populacao,
            pib,
            rendimento_mensal
        ])

wb = Workbook()
ws = wb.active
ws.title = "Municípios por UF"

ws.append(["Cod_IBGE_UF", "Nome_UF", "Sigla_UF", "Cod_IBGE_Município", "Nome_Município", "População", "PIB", "Rendimento Mensal"])

for row in dados_municipios:
    ws.append(row)

wb.save('municipios_por_uf.xlsx')
print('Excel gerado com sucesso, disponibilizado na pasta de scripts')
