# Generated by Django 4.2.7 on 2024-10-02 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cats", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Cats",
            new_name="Cat",
        ),
    ]
