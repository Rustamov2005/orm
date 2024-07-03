from django.contrib import admin
from .models import Book, Author, Comments, Adress

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Comments)
admin.site.register(Adress)

