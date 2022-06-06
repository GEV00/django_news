from django.urls import path
from app_media.views import UploadFile

urlpatterns = [
    path('upload_file/', UploadFile.as_view(), name='upload_file')
]
