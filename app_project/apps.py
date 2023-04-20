from django.apps import AppConfig


class AppProjectConfig(AppConfig):
    name = 'app_project'

    def ready(self):
        # Import celery app now that Django is mostly ready.
        # This initializes Celery and autodiscovers tasks
        import project_manager.celery
