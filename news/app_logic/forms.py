from django import forms


class EmailSendForm(forms.Form):
    mail_to = forms.EmailField(label='Получатель', required=True)