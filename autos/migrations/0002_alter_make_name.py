# Generated by Django 4.2.7 on 2024-10-01 10:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="make",
            name="name",
            field=models.CharField(
                help_text="Enter a make (e.g. Renault)",
                max_length=200,
                validators=[
                    django.core.validators.MinLengthValidator(
                        2, "Make must be greater than 1 character "
                    )
                ],
            ),
        ),
    ]
