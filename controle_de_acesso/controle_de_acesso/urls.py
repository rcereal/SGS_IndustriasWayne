from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sistema_de_seguranca/', include('sistema_de_seguranca.urls')),
]
