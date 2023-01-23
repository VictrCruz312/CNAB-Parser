from django.shortcuts import render, redirect

from .forms import UploadFileForm
from .models import CNABMovimentation
from .serializers import CNABMovimentationSerializer
import ipdb


def upload_file(request):
    if request.method == "POST":
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

            return redirect("listMovimentation/")
    else:
        form = UploadFileForm()
    return render(request, "cnab_upload/upload.html", {"form": form})


def listMovimentation(request):
    return render(request, "cnab_upload/listMovimentation.html")
