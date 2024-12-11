from django.apps import AppConfig


class PickupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Pickup'

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    def ready(self):
        import users.signals
