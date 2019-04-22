from django.conf import settings
from django.db import migrations
from django.contrib.auth import get_user_model


def forward(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Profile = apps.get_model("profiles", "Profile")
    db_alias = schema_editor.connection.alias
    for user in User.objects.using(db_alias).all():
        profile, created = Profile.objects.using(db_alias).get_or_create(user=user)


def reverse(apps, schema_editor):
	pass


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forward, reverse)
    ]

