from unicodedata import category
from django.contrib import admin
from .models import Article, Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Category, CategoryAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','publish','status','category_to_str')
    list_filter = ('publish','status')
    search_fields = ('title','description')
    prepopulated_fields = {'slug': ('title',)}

    def category_to_str(self, obj):
        return [category.title for category in obj.category.all()]



admin.site.register(Article, ArticleAdmin)



