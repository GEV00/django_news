from django.http import HttpResponse
from django.shortcuts import render
from app_media.forms import UploadFileForm
from django.views import View


class UploadFile(View):
    
    def get(self, request):
        
        upload_file_form = UploadFileForm

        return render(request, 'app_media/upload_page.html', context={'form':upload_file_form})

    def post(self, request):
        print('FLAG')
        upload_file_form = UploadFileForm(request.POST, request.FILES)

        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=[file.name,'<br>', file.size], status=200)

        return render(request, 'app_media/upload_page.html', context={'form':upload_file_form})


