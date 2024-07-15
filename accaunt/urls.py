from django.urls import path
from .views import dokon, tarix, accaunt, profil
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dokon/', dokon, name='dokon'),
    path('tarix/', tarix, name='tarix'),
    path('accaunt/', accaunt, name='accaunt'),
    path('profil/', profil, name='profil'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)