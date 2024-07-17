from django.urls import path
from .views import boook, author, comments, users, adreslar, book_detail, create_book, book_detail_viwe, book_delete_viwe


urlpatterns = [
    path('books/', boook, name='book'),
    path('author/', author, name='author'),
    path('commints/', comments, name='comments'),
    path('users/', users, name='users'),
    path('address/', adreslar, name='address'),
    path('book/<slug:slug>/', book_detail, name='book_detail'),
    path('create_book/', create_book, name='create_book'),
    path('booklar/<int:id>', book_detail_viwe, name='book_detail_viwe'),
    path('booklar/detete/<int:id>', book_delete_viwe, name='book_delete_viwe'),

]