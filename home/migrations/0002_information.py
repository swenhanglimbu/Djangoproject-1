# Generated by Django 4.1.4 on 2022-12-22 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Information",
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
                ("address1", models.CharField(max_length=300)),
                ("address2", models.CharField(max_length=300)),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=100)),
                ("time", models.CharField(max_length=200)),
            ],
        ),
    ]
