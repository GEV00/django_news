from re import template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from newspaper.models import Comments, News,Tags
from newspaper.forms import CommentForm, NewsForm
from django.views.generic import ListView, DetailView

# Create your views here.

class NewsView(ListView):
    
    model = News
    context_object_name = 'news_list'
    template_name = 'newspaper/index.html'
    #переопределяем метод get_context_data для определения дополнительных
    #ключей context помимо news_list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        context['tags'] = Tags.objects.all()
        return context
    #переопредяем метод get_queryset для фильтрации ативных новостей
    def get_queryset(self):
        if self.request.GET.get('sorted')=='1': #проверка наличия параметра в строке для фильтрации по дате
            return News.objects.filter(active=True).order_by('created_at')
        return News.objects.filter(active=True)

#Представление для фильтрации новостей по тегам
class NewsViewTag(ListView):

    model = News
    context_object_name = 'news_list'
    template_name = 'newspaper/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        context['tags'] = Tags.objects.all()
        return context
    #переопределяем метод get_queryset для выдачи новостей с выбранными тегами
    #и при этом активными
    #tag _ _ id значит что фильтруем по id связанной модели, заданной в поле tag
    def get_queryset(self):
        if self.request.GET.get('sorted')=='1':#проверка передаваемого параметра из строки ссылки
            print(self.request.GET.get('sorted'))
            return News.objects.filter(tag__id=self.kwargs['tag_id'], active=True).order_by('created_at')
        return News.objects.filter(tag__id=self.kwargs['tag_id'], active=True)


def news_older(request):
    #принимаем сортированный по дата публикации новости из модели
    news_list = News.objects.filter(active=True).order_by('created_at')
    tags = Tags.objects.all()

    return render(request, 'newspaper/index_old.html', context={'news_list':news_list,
                                                                'tags':tags})


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
            return HttpResponseRedirect('/newspaper/')
        
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
            if not request.user.is_authenticated:
                username = comment_form.cleaned_data['username']
                comment_form.cleaned_data['username'] = f"{username} (аноним)"
            comment_form.cleaned_data['new_id'] = news_id
            Comments.objects.create(**comment_form.cleaned_data)
            #редирект к комментируемой новости (просто шаг назад)
            return HttpResponseRedirect('../')
        return render(request, 'newspaper/create_comment.html', context={'comment_form':comment_form})