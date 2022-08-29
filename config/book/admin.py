from django.contrib import admin
from book.models import post
from book.models import read

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','slug','date_of_brith')
    prepopulated_fields = {'slug': ('title',)}


class ReadAdmin(admin.ModelAdmin):
    list_display = ('title','slug','publish','status')
    list_filter = ('publish','status')
    search_fields = ('title','description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(post, PostsAdmin)
admin.site.register(read, ReadAdmin)