from django.shortcuts import render, redirect
from .forms import UploadFileForm
import ipdb


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            file = [*request.FILES["file"]]

            for movimentation in file:
                ...
            return redirect("success")
    else:
        form = UploadFileForm()
    return render(request, "cnab_upload/upload.html", {"form": form})
