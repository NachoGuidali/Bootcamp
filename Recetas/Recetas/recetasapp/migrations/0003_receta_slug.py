# Generated by Django 4.1.7 on 2023-04-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetasapp', '0002_alter_receta_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
