# Generated by Django 4.1.1 on 2022-10-24 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("measurements", "0003_alter_equipment_connection_scpi_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Equipment_Parameter",
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
            ],
        ),
        migrations.RenameModel(
            old_name="Equipment_Details", new_name="Equipment_Detail",
        ),
        migrations.DeleteModel(name="Equipment_Parameters",),
        migrations.AddField(
            model_name="equipment_parameter",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="measurements.equipment_detail",
            ),
        ),
    ]
