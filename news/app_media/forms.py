from django import forms
from django.core.exceptions import ValidationError


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=20, required=True)
    description = forms.CharField(max_length=30, required=False)
    file = forms.FileField()


class CheackFileForm(forms.Form):
    file = forms.FileField(help_text='добавьте файл для проверки')

    def clean_file(self):
        file = self.cleaned_data['file']
        for ban_word in ['Это', 'Слово', 'Нельзя', 'Использовать']: #сначала проверяем название
            if ban_word.lower() in file.name.lower():
                #print('name')
                raise ValidationError('Название файла не удовлетворяет требованиям')

        #потом проверяем содержание
        with file.open() as f:
            for line in f.readlines():
                for ban_word in ['Это', 'Слово', 'Нельзя', 'Использовать']:
                    if ban_word.lower() in line.decode().lower():
                        print('data')
                        raise ValidationError('Содержание файла не удовлетворяет требованиям')

        return file

