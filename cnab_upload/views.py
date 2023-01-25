from django.shortcuts import render, redirect
from django.views import View

from .forms import UploadFileForm
from .models import CNABMovimentation
from .serializers import CNABMovimentationSerializer, ListMovimentationSerializer
import ipdb


class UploadFileView(View):
    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            type_dict = {
                1: ["Débito", "+"],
                2: ["Boleto", "-"],
                3: ["Financiamento", "-"],
                4: ["Crédito", "+"],
                5: ["Recebimento Empréstimo", "+"],
                6: ["vendas", "+"],
                7: ["Recebimento TED", "+"],
                8: ["Recebimento DOC", "+"],
                9: ["Aluguel", "-"],
            }

            file = [item.decode().strip() for item in [*request.FILES["file"]]]
            new_file = []
            for movimentation in file:
                convert = {
                    "Tipo": type_dict[int(movimentation[0:1])][0],
                    "operacao": type_dict[int(movimentation[0:1])][1],
                    "Data": f"{movimentation[1:9][:4]}-{movimentation[1:9][4:6]}-{movimentation[1:9][6:8]}",
                    "Valor": int(movimentation[9:19]) / 100,
                    "CPF": movimentation[19:30],
                    "Cartão": movimentation[30:42],
                    "Hora": f"{movimentation[42:48][:2]}:{movimentation[42:48][2:4]}:{movimentation[42:48][4:6]}",
                    "Dono_da_loja": movimentation[48:62].strip(),
                    "Nome_da_loja": movimentation[62:81].strip(),
                }
                new_file.append(convert)

            serializer = CNABMovimentationSerializer(data=new_file, many=True)

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return self.get(request)

        else:
            return render(request, "cnab_upload/upload.html", {"form": form})

    def get(self, request):
        form = UploadFileForm()

        items = CNABMovimentation.objects.all()

        # setando lista de lojas que contem nos items:
        lojas = set()

        for item in items:
            lojas.add(item.Nome_da_loja)

        # filtrando a lista caso tenha o filtro:
        storeFilter = request.GET.get("store")

        if storeFilter:
            items = items.filter(Nome_da_loja=storeFilter)
            lojas.remove(storeFilter)
        else:
            storeFilter = "Selecione a loja"

        store_balances = {}

        for item in items:
            store = item.Nome_da_loja
            balance = item.Valor
            if item.operacao == "+":
                if store in store_balances:
                    store_balances[store] += balance
                else:
                    store_balances[store] = balance
            else:
                if store in store_balances:
                    store_balances[store] -= balance
                else:
                    store_balances[store] = -balance

        items = [
            item
            for item in items
            if store_balances.get(item.Nome_da_loja, None) is not None
        ]

        for item in items:
            item.balance = store_balances[item.Nome_da_loja]

        return render(
            request,
            "cnab_upload/upload.html",
            {"form": form, "items": items, "lojas": lojas, "filter": storeFilter},
        )
