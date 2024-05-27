from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Estado
from .facade import format_moeda, format_populacao

class EstadoDetailView(APIView):
    """
    Endpoint para retornar detalhes de um estado específico.

    Parameters:
        request (Request): Requisição HTTP.
        estado_sigla (str): Sigla do estado enviado pelo front.

    Returns:
        Response: Um objeto de resposta HTTP contendo os detalhes do estado, incluindo sua população,
        PIB, rendimento mensal e a contagem de municípios pertencentes a esse estado formatados para 
        retornar em string com tratamentos de formatação.
    """
    def get(self, request, estado_sigla):
        try:
            estado = Estado.objects.get(sigla=estado_sigla)
        except Estado.DoesNotExist:
            return Response({"error": "Estado não encontrado"}, status=404)

        estado_data = {
            'id': estado.id,
            'nome': estado.nome,
            'sigla': estado.sigla,
            'quantidade_municipios': estado.municipios.count(),
            'populacao': format_populacao(estado.populacao),
            'pib': format_moeda(estado.pib),
            'rendimento_mensal': format_moeda(estado.rendimento_mensal),
        }
        
        return Response(estado_data)

class EstadosListView(APIView):
    """
    Endpoint para retornar uma lista de objetos contendo os estados e respectivos dados.

    Parameters:
        request (Request): Requisição HTTP.

    Returns:
        Response: Um objeto de resposta HTTP contendo uma lista de dicionários,
        cada um representando um estado e sua quantidade de municípios, população,
        PIB e rendimento mensal médio.
    """
    def get(self, request):
        estados = Estado.objects.all()
        estados_data = []

        for estado in estados:
            estado_data = {
                'id': estado.id,
                'nome': estado.nome,
                'sigla': estado.sigla,
                'quantidade_municipios': estado.municipios.count(),
                'populacao': estado.populacao / 100000,
                'pib': estado.pib / 10000000,
                'rendimento_mensal': estado.rendimento_mensal / 10,
            }
            estados_data.append(estado_data)
        
        return Response(estados_data)