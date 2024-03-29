from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index',),
    path('<int:contato_id>', views.contato, name='contato',),
    path('busca/', views.busca, name='busca',),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#  texto acima faz importar imagens