from django.apps import AppConfig
from django.core.cache import cache


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        # Clear the cache when the application starts
        cache.clear()
