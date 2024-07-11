from django.urls import path
from .views import kitob, kutibxona, users


urlpatterns = [
    path('kitob/', kitob, name='kitob'),
    path('kutib/', kutibxona, name='kutib'),
    path('usere/', users, name='users'),
]