from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.style import context
from requests import request
from app_media.forms import UploadFileForm, CheackFileForm
from django.views import View


class UploadFile(View):
    
    def get(self, request):
        
        upload_file_form = UploadFileForm

        return render(request, 'app_media/upload_page.html', context={'form':upload_file_form})

    def post(self, request):

        upload_file_form = UploadFileForm(request.POST, request.FILES)

        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=[file.name,'<br>', file.size], status=200)

        return render(request, 'app_media/upload_page.html', context={'form':upload_file_form})


class CheakFile(View):

    def get(self, request):

        cheak_file_form = CheackFileForm

        return render(request, 'app_media/cheak_file_page.html', context={'form':cheak_file_form})

    def post(self, request):

        cheak_file_form = CheackFileForm(request.POST, request.FILES)

        if cheak_file_form.is_valid():
            return HttpResponse(content='Все хорошо!', status=200)

        return HttpResponse(content=['Файл не прошел проверку!', cheak_file_form.errors])