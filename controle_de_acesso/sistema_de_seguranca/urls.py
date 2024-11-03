from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Página inicial
    path('login/', views.user_login, name='login'),  # Login
    path('logout/', views.user_logout, name='logout'),  # Logout
    path('recursos/', views.lista_de_recursos, name='lista_de_recursos'),
    path('adicionar_recurso/', views.adicionar_recurso, name='adicionar_recurso'),
    path('editar_recurso/<int:recurso_id>/', views.editar_recurso, name='editar_recurso'),
    path('recursos/excluir/<int:recurso_id>/', views.excluir_recurso, name='excluir_recurso'),
    path('solicitar-recuperacao-senha/', views.solicitar_recuperacao_senha, name='solicitar_recuperacao_senha'),
    path('redefinir-senha/<str:codigo_recuperacao>/', views.redefinir_senha, name='redefinir_senha'),
]
