from django.apps import AppConfig


class ClientipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientip'

    def ready(self):
        import clientip.signals
