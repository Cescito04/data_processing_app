# Generated by Django 3.1.12 on 2025-04-13 01:58

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion

def get_default_user():
    from django.contrib.auth import get_user_model
    User = get_user_model()
    admin = User.objects.filter(is_superuser=True).first()
    if admin:
        return admin.id
    return 1

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_processor', '0002_datafile_original_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='user',
            field=models.ForeignKey(
                default=get_default_user,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='data_files',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Utilisateur',
            ),
        ),
    ]
