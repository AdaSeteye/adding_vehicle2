# Generated by Django 4.1.3 on 2024-04-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("add_vehicle", "0003_vehicle_edvla_renewal_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicle",
            name="document_renewal_date",
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="libre_number",
            field=models.CharField(max_length=100),
        ),
    ]