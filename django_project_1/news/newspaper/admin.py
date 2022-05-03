from atexit import register
from django.contrib import admin
from newspaper.models import News, Comments
# Register your models here.
@admin.register(News, Comments)
class ModelAdmin(admin.ModelAdmin):
    pass