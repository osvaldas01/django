# Generated by Django 5.0 on 2023-12-19 16:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("country", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="city",
            old_name="continent",
            new_name="country",
        ),
    ]
