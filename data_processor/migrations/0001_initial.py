# Generated by Django 4.2.20 on 2025-04-02 20:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="uploads/%Y/%m/%d/", verbose_name="Fichier"
                    ),
                ),
                (
                    "original_filename",
                    models.CharField(
                        max_length=255, verbose_name="Nom du fichier original"
                    ),
                ),
                (
                    "upload_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Date d'importation",
                    ),
                ),
                (
                    "file_type",
                    models.CharField(max_length=10, verbose_name="Type de fichier"),
                ),
                (
                    "processed",
                    models.BooleanField(default=False, verbose_name="Traité"),
                ),
                (
                    "row_count",
                    models.IntegerField(default=0, verbose_name="Nombre de lignes"),
                ),
                (
                    "column_count",
                    models.IntegerField(default=0, verbose_name="Nombre de colonnes"),
                ),
                (
                    "missing_values",
                    models.JSONField(default=dict, verbose_name="Valeurs manquantes"),
                ),
                (
                    "outliers",
                    models.JSONField(default=dict, verbose_name="Valeurs aberrantes"),
                ),
                (
                    "processing_summary",
                    models.JSONField(default=dict, verbose_name="Résumé du traitement"),
                ),
            ],
            options={
                "verbose_name": "Fichier de données",
                "verbose_name_plural": "Fichiers de données",
                "ordering": ["-upload_date"],
            },
        ),
    ]
