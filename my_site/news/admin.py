from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')#какие поля в админке будут ссылкой
    search_fields = ('title', 'content')# поля по которым можно осуществлять поиск
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')#по каким полям фильрация в админке

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')#какие поля в админке будут ссылкой
    search_fields = ('title',)# поля по которым можно осуществлять поиск,

admin.site.register(News, NewsAdmin)#регистрация в админке, класс-редактор NewsAdmin должен идти после основной модели
admin.site.register(Category, CategoryAdmin)