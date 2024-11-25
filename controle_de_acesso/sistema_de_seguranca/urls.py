from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),  
    path('login/', views.user_login, name='login'), 
    path('logout/', views.user_logout, name='logout'), 
    path('recursos/', views.lista_de_recursos, name='lista_de_recursos'),
    path('adicionar_recurso/', views.adicionar_recurso, name='adicionar_recurso'),
    path('editar_recurso/<int:recurso_id>/', views.editar_recurso, name='editar_recurso'),
    path('recursos/excluir/<int:recurso_id>/', views.excluir_recurso, name='excluir_recurso'),
    path('recurso/detalhes/<int:recurso_id>', views.detalhes_recurso, name='detalhes_recurso'),
    path('solicitar-recuperacao-senha/', views.solicitar_recuperacao_senha, name='solicitar_recuperacao_senha'),
    path('redefinir-senha/<str:codigo_recuperacao>/', views.redefinir_senha, name='redefinir_senha'),
    path('adicionar-usuario/', views.adicionar_usuario, name='adicionar_usuario'),
    path('gerenciar-usuario/<int:user_id>/', views.gerenciar_usuario, name='gerenciar_usuario'),
    path('editar-usuario/<int:user_id>/', views.gerenciar_usuario, name='gerenciar_usuario_editar'),
    path('excluir-usuario/<int:user_id>/', views.excluir_usuario, name='excluir_usuario'),
    path('lista-usuarios/', views.lista_de_usuarios, name='lista_de_usuarios'),
    path('perfil/', views.perfil_view, name='profile'),
    path('detalhes_usuario/<int:user_id>/', views.detalhes_usuario, name='detalhes_usuario'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
