from atexit import register
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from newspaper.models import News, Comments, Tags
# Register your models here.


class TagsAdmin(admin.ModelAdmin):
    list_display = ['title']
#Применяем класс Tabular(Stacked)Inline к модели, в которой описана
#связь ForeignKey. В нашем случае в Commets есть поле new - связь
#ForeignKey с News.
class CommentsInLine(admin.TabularInline):
    model = Comments

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag','created_at', 'updated_at', 'active']
    list_filter = ['active', 'tag']
    #Подвязываем inlines через одноименное поле
    inlines = [CommentsInLine]
    #Описываем групповые дейстия:
    #список действий
    actions = ['activate', 'deactivate']
    #описание первого действия
    def activate(self, request, queryset):
        if not request.user.has_perm('newspaper.can_activate'):
            return PermissionDenied('У вас нет прав для совершения этого действия')
        queryset.update(active=True)
    #описание второго дейтсвия
    def deactivate(self, request, queryset):
        if not request.user.has_perm('newspaper.can_activate'):
            return PermissionDenied('У вас нет прав для совершения этого действия')
        queryset.update(active=False)
    #визуализация действий в админке в выпадающем списке
    activate.short_description = 'Перевести новость в Активные'
    deactivate.short_description = 'Убрать новость из Активных'

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['username', 'content', 'new', 'delete_status']
    list_filter = ['username']

    actions = ['deleted', 'non_deleted']

    def deleted(self, request, queryset):
        queryset.update(delete_status=True)
    
    def non_deleted(self, request, queryset):
        queryset.update(delete_status=False)

    deleted.short_description = 'Пометить как "Удаленный администратором"'
    non_deleted.short_description = 'Убрать отметку об удалении'

admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Tags, TagsAdmin)