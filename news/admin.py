from django.contrib import admin

from news.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')
    prepopulated_fields = {'slug': ('name',)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date')
    prepopulated_fields = {'slug': ('title',)}
    

    admin.site.register(Category)
    admin.site.register(News)