# Generated by Django 4.2.5 on 2024-01-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                    "slug",
                    models.SlugField(unique=True, verbose_name="Уникальное название"),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Название")),
                (
                    "image",
                    models.ImageField(upload_to=None, verbose_name="Изображение"),
                ),
                ("desc", models.TextField(verbose_name="Описание")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="Цена"
                    ),
                ),
            ],
        ),
    ]