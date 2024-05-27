import openpyxl
from django.core.management.base import BaseCommand
from api.models import Estado, Municipio

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        file_path = 'dashboard_ibge/scripts/municipios_por_uf.xlsx'

        wb = openpyxl.load_workbook(file_path)
        ws = wb['Municípios por UF']

        for row in ws.iter_rows(min_row=2, values_only=True):
            cod_ibge_uf, nome_uf, sigla_uf, cod_ibge_municipio, nome_municipio, populacao, pib, rendimento_mensal = row

            estado, created = Estado.objects.get_or_create(
                cod_ibge=cod_ibge_uf,
                defaults={'nome': nome_uf, 'sigla': sigla_uf}
            )

            Municipio.objects.create(
                cod_ibge=cod_ibge_municipio,
                nome=nome_municipio,
                estado=estado,
                populacao=populacao,
                pib=pib,
                rendimento_mensal=rendimento_mensal
            )

            print(f'Município {nome_municipio} adicionado ao estado {nome_uf}.')

        print('Dados populados com sucesso.')