from django.db import models

class Estado(models.Model):
    cod_ibge = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Municipio(models.Model):
    cod_ibge = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='municipios')
    populacao = models.IntegerField()
    pib = models.FloatField()
    rendimento_mensal = models.FloatField()

    def __str__(self):
        return self.nome