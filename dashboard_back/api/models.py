from django.db import models


class Estado(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)
    populacao = models.IntegerField()
    pib = models.BigIntegerField()
    rendimento_mensal = models.FloatField()

    def __str__(self):
        return self.nome

class Municipio(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, related_name='municipios', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome