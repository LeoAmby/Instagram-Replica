from django.apps import AppConfig


class StartappConfig(AppConfig):
    name = 'startApp'

    def ready(self):
        import startApp.signals
