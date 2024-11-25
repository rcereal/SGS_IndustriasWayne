from django.apps import AppConfig


class SistemaDeSegurancaConfig(AppConfig):
    name = 'sistema_de_seguranca'

    def ready(self):
        import sistema_de_seguranca.signals 

