from django.contrib import admin
from .models import Category, Blog

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','uddated') 

class BlogAdmin(admin.ModelAdmin):#configuracion extendida
    readonly_fields=('created','updated') 
    list_display=('title','author','published')
    ordering= ('author','published')
    search_fields=('titule',)
    date_hierarchy='published'
    list_filter=('author__username','categories__name')

admin.site.register(Category)
admin.site.register(Blog)