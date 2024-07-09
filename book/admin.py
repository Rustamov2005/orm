from django.contrib import admin
from .models import Book, Author, Comments, Adress
from import_export.admin import ImportExportModelAdmin

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'price', 'discriptions', 'count', 'created_at')
    list_display_links = ('title', 'price', 'discriptions', 'count', 'created_at')
    search_fields = ('title', 'price')
    ordering = ('-title',)

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'created_at')
    list_display_links = ('first_name', 'last_name', 'date_of_birth', 'created_at')
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name', 'first_name')

@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'text', 'created_at')
    list_display_links = ('user', 'text', 'created_at')
    search_fields = ('user', 'text')
    ordering = ('-user', 'text')

admin.site.register(Adress)