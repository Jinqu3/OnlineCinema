# Generated by Django 5.0.3 on 2024-04-16 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0008_film_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='film_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.film'),
        ),
        migrations.DeleteModel(
            name='FilmPhoto',
        ),
    ]