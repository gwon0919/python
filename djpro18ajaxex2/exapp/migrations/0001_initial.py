# Generated by Django 5.0a1 on 2023-10-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Producttab",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("category", models.CharField(blank=True, max_length=50, null=True)),
                ("pname", models.CharField(blank=True, max_length=50, null=True)),
                ("price", models.CharField(blank=True, max_length=50, null=True)),
                ("stock", models.CharField(blank=True, max_length=50, null=True)),
                ("description", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "db_table": "producttab",
                "managed": False,
            },
        ),
    ]
