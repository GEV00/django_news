from re import template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from newspaper.models import Comments, News
from newspaper.forms import CommentForm, NewsForm
from django.views.generic import ListView, DetailView

# Create your views here.

class NewsView(ListView):
    
    model = News
    context_object_name = 'news_list'
    template_name = 'newspaper/index.html'



class NewsDetail(View):

    def get(self, request, news_id):

        news_data = News.objects.get(id=news_id)
        #ЧЕРЕЗ ФИЛЬТР ПОЛУЧАЕМ ВСЕ КОММЕНТЫ ДЛЯ НОВОСТИ С ПЕРЕДАВАЕМЫМ ID:
        comments = Comments.objects.filter(new_id=news_id)

        return render(request, 'newspaper/news_detail.html', context={'news_data':news_data,
                                                                     'comments':comments})



class NewsCreate(View):

    def get(self, request):

        news_form = NewsForm()

        return render(request, 'newspaper/create_news.html', context={'news_form':news_form})

    def post(self, request):

        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')
        
        return render(request, 'newspaper/create_news.html', context={'news_form':news_form})



class NewsEdit(View):

    def get(self, request, news_id):
        #берем данные из БД по id
        news = News.objects.get(id = news_id)
        #вставляем в форму
        news_form = NewsForm(instance=news)

        return render(request, 'newspaper/news_edit.html', context={'news_form':news_form})

    def post(self, request, news_id):
        #берем данные из БД по id
        news = News.objects.get(id = news_id)
        #вставляем в форму по постзапросу
        news_form = NewsForm(request.POST, instance=news)
        #проверяем валидность формы
        if news_form.is_valid():
            #если форма валидна, сохранаяем данные в модель
            news.save()
            return HttpResponseRedirect('../')
        return render(request,'newspaper/news_edit.html', context={'news_form':news_form})



class CommentCreate(View):

    def get(self, request, news_id):

        comment_form = CommentForm()

        return render(request, 'newspaper/create_comment.html', context={'comment_form':comment_form})

    def post(self, request, news_id):

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.cleaned_data['new_id'] = news_id
            Comments.objects.create(**comment_form.cleaned_data)
            #редирект к комментируемой новости (просто шаг назад)
            return HttpResponseRedirect('../')

        return render(request, 'newspaper/create_comment.html', context={'comment_form':comment_form})