from django.apps import AppConfig


class SistemaDeSegurancaConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'sistema_de_seguranca'

    def ready(self):
        import sistema_de_seguranca.signals 

