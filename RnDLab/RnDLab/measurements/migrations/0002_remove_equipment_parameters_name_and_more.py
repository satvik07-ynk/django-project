# Generated by Django 4.1.1 on 2022-10-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("measurements", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="equipment_parameters", name="name",),
        migrations.AddField(
            model_name="equipment_parameters",
            name="name",
            field=models.ManyToManyField(to="measurements.equipment_type"),
        ),
    ]
