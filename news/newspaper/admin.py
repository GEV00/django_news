from atexit import register
from django.contrib import admin
from newspaper.models import News, Comments
# Register your models here.

#Применяем класс Tabular(Stacked)Inline к модели, в которой описана
#связь ForeignKey. В нашем случае в Commets есть поле new - связь
#ForeignKey с News.
class CommentsInLine(admin.TabularInline):
    model = Comments

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    #Подвязываем inlines через одноименное поле
    inlines = [CommentsInLine]

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'username']
    list_filter = ['username']

admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)