from django.apps import AppConfig
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model



class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals