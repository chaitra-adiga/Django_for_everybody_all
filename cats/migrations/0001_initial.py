# Generated by Django 4.2.7 on 2024-10-01 10:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Breed",
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
                    "name",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, "Breed must be greater than ! character"
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cats",
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
                    "nickname",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                1, "Your cat loves You ! give it a nickname Dang it!!"
                            )
                        ],
                    ),
                ),
                ("weight", models.PositiveIntegerField()),
                ("foods", models.CharField(max_length=300)),
                (
                    "breed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cats.breed"
                    ),
                ),
            ],
        ),
    ]
