# Generated by Django 4.1 on 2022-09-03 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Size",
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
                    "title",
                    models.CharField(
                        choices=[("1", "Small"), ("2", "Medium"), ("3", "Large")],
                        max_length=1,
                        verbose_name="Size",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pizza",
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
                ("topping1", models.CharField(max_length=30, verbose_name="Topping_1")),
                ("topping2", models.CharField(max_length=30, verbose_name="Topping_2")),
                (
                    "size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pizza.size"
                    ),
                ),
            ],
        ),
    ]
