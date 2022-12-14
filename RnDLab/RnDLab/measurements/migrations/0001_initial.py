# Generated by Django 4.1.1 on 2022-10-24 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Equipment_Details",
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
                    models.CharField(max_length=120, verbose_name="Equipment Name"),
                ),
                (
                    "weblink",
                    models.URLField(blank=True, verbose_name="Website Address"),
                ),
                (
                    "datasheet",
                    models.URLField(blank=True, verbose_name="Datasheet Address"),
                ),
                ("scpilink", models.URLField(blank=True, verbose_name="SCPI Address")),
            ],
        ),
        migrations.CreateModel(
            name="Equipment_Type",
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
                ("source_equipment", models.BooleanField()),
                ("measurement_equipment", models.BooleanField()),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="measurements.equipment_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Equipment_Parameters",
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
                ("measurement_parameter", models.CharField(blank=True, max_length=100)),
                ("source_parameter", models.CharField(blank=True, max_length=100)),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="measurements.equipment_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Equipment_Connection",
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
                ("scpi_address", models.CharField(max_length=300)),
                ("status", models.BooleanField()),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="measurements.equipment_details",
                    ),
                ),
            ],
        ),
    ]
