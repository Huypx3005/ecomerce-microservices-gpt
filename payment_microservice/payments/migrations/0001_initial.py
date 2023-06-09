# Generated by Django 4.2 on 2023-04-24 03:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("card_number", models.CharField(max_length=16)),
                ("card_exp_month", models.CharField(max_length=2)),
                ("card_exp_year", models.CharField(max_length=4)),
                ("card_cvv", models.CharField(max_length=3)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
