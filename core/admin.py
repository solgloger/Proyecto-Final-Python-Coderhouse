from django.contrib import admin
from .models import Author, Post, Tag
# Register your models here.

class PostInline(admin.TabularInline):
    model = Post
    extra = 1

@admin.register (Author)
class AuthorAdmin (admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)
    inlines = [PostInline]

@admin.register (Tag)
class TagAdmin (admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register (Post)
class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author__name', 'tags__name')
    list_filter = ('published_date', 'author')
    filter_horizontal = ("tags",)


