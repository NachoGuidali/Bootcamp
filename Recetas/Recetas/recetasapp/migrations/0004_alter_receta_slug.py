# Generated by Django 4.1.7 on 2023-04-27 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetasapp', '0003_receta_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]