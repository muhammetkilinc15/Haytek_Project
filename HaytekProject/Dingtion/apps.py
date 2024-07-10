from django.apps import AppConfig


class DingtionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Dingtion'

    def ready(self):
        import Dingtion.signals  # Sinyal dosyanızın yüklenmesi