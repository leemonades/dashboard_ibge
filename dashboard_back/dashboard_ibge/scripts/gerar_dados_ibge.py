import requests
from openpyxl import Workbook

dados_municipios = []
codigos_estados = [
    12, 27, 13, 16, 29, 23, 53, 32, 21, 52, 31, 50, 15, 25, 51, 26, 22,
    33, 24, 11, 14, 43, 41, 42, 35, 28, 17
]

for codigo_estado in codigos_estados:
    url_municipios = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{codigo_estado}/municipios'
    

    response_municipios = requests.get(url_municipios)
    municipios = response_municipios.json()

    for municipio in municipios:
        dados_municipios.append([
            municipio['microrregiao']['mesorregiao']['UF']['id'],
            municipio['microrregiao']['mesorregiao']['UF']['nome'],
            municipio['microrregiao']['mesorregiao']['UF']['sigla'],
            municipio['id'],
            municipio['nome']
        ])


wb = Workbook()
ws = wb.active
ws.title = "Municípios por UF"


ws.append(["Cod_IBGE_UF", "Nome_UF", "Sigla_UF", "Cod_IBGE_Município", "Nome_Município"])
for row in dados_municipios:
    ws.append(row)
wb.save('municipios_por_uf.xlsx')
print('Excel gerado com sucesso, disponibilizado na pasta de scripts')
