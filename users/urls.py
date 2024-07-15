from django.urls import path
from .views import login_vewes, regeter_vewes, logout_vewes


urlpatterns = [
    path('login/', login_vewes, name='login'),
    path('register/', regeter_vewes, name='register'),
    path('logout/', logout_vewes, name='logout'),

]