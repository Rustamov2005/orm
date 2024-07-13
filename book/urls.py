from django.urls import path
from .views import boook, author, comments, users, adreslar, book_detail


urlpatterns = [
    path('books/', boook, name='book'),
    path('author/', author, name='author'),
    path('commints/', comments, name='comments'),
    path('users/', users, name='users'),
    path('address/', adreslar, name='address'),
    path('book/<slug:slug>/', book_detail, name='book_detail'),

]