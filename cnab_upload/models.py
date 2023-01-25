from django.db import models
import uuid


class TypeChoice(models.TextChoices):
    Débito = "Débito"
    Boleto = "Boleto"
    Financiamento = "Financiamento"
    Crédito = "Crédito"
    Recebimento_Empréstimo = "Recebimento Empréstimo"
    vendas = "vendas"
    Recebimento_TED = "Recebimento TED"
    Recebimento_DOC = "Recebimento DOC"
    Aluguel = "Aluguel"


class CNABMovimentation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Tipo = models.CharField(choices=TypeChoice.choices, max_length=25)
    operacao = models.CharField(max_length=1)
    Data = models.DateField()
    Valor = models.DecimalField(max_digits=10, decimal_places=2)
    CPF = models.CharField(max_length=11)
    Cartão = models.CharField(max_length=12)
    Hora = models.TimeField()
    Dono_da_loja = models.CharField(max_length=14)
    Nome_da_loja = models.CharField(max_length=19)
