# Generated by Django 4.1.3 on 2024-04-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vehicle",
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
                ("chassis_number", models.CharField(max_length=100)),
                ("libre_number", models.CharField(max_length=100)),
                ("document_renewal_date", models.DateField()),
                ("insurance_renewal_date", models.DateField()),
            ],
        ),
    ]
