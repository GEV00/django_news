from django import forms
from newspaper.models import News, Comments

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('username', 'content')