from django.contrib import admin
from .models import Word,Comment

# Register your models here.

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('eentry','ecat','tentry')
    list_filter = ('ecat',)
    ordering = ('eentry',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('word','comment','user','ts')