# Generated by Django 4.2.20 on 2025-04-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data_processor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="datafile",
            name="original_file_type",
            field=models.CharField(
                default="unknown",
                max_length=10,
                verbose_name="Type de fichier original",
            ),
        ),
    ]
