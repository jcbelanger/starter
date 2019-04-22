import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model


def profile_image_upload_to(profile, filename):
    name, ext = os.path.splitext(filename)
    return f'profiles/image/user_{profile.user.id}{ext}'


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to=profile_image_upload_to, blank=True)

    class Meta:
        ordering = ['user__date_joined']

    def get_absolute_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.pk})
