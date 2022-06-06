from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=20, required=True)
    description = forms.CharField(max_length=30, required=False)
    file = forms.FileField()
