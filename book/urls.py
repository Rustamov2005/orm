from django.urls import path
from .views import boook, author, comments, users, address





urlpatterns = [
    path('', boook, name='book'),
    path('author/', author, name='author'),
    path('commints/', comments, name='comments'),
    path('users/', users, name='users'),
    path('address/', address, name='address'),

]