# Generated by Django 4.1.5 on 2023-01-23 18:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CNABMovimentation",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "Tipo",
                    models.CharField(
                        choices=[
                            ("Débito", "Débito"),
                            ("Boleto", "Boleto"),
                            ("Financiamento", "Financiamento"),
                            ("Crédito", "Crédito"),
                            ("Recebimento Empréstimo", "Recebimento Empréstimo"),
                            ("vendas", "Vendas"),
                            ("Recebimento TED", "Recebimento Ted"),
                            ("Recebimento DOC", "Recebimento Doc"),
                            ("Aluguel", "Aluguel"),
                        ],
                        max_length=25,
                    ),
                ),
                ("operacao", models.CharField(max_length=1)),
                ("Data", models.DateField()),
                ("Valor", models.DecimalField(decimal_places=2, max_digits=10)),
                ("CPF", models.CharField(max_length=11)),
                ("Cartão", models.CharField(max_length=12)),
                ("Hora", models.TimeField()),
                ("Dono_da_loja", models.CharField(max_length=14)),
                ("Nome_da_loja", models.CharField(max_length=19)),
            ],
        ),
    ]
