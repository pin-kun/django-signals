from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    # to run the signals (also added default_app_config in __init__.py)
    def ready(self):
        import blog.signals