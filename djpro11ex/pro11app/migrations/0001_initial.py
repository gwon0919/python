# Generated by Django 5.0a1 on 2023-10-23 03:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Familydb",
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
                ("name", models.CharField(max_length=50)),
                ("nai", models.IntegerField(max_length=50)),
                ("tel", models.CharField(max_length=50)),
                ("gen", models.CharField(max_length=50)),
            ],
        ),
    ]