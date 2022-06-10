from django.urls import path
from app_media.views import UploadFile, CheakFile

urlpatterns = [
    path('upload_file/', UploadFile.as_view(), name='upload_file'),
    path('cheak/', CheakFile.as_view(), name='cheak_file')
]
