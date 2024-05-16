# Generated by Django 5.0.3 on 2024-05-14 22:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0017_film_reviews'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='user',
            name='reviews',
            field=models.ManyToManyField(related_name='user_reviews', through='cinema.Review', to='cinema.film'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to='cinema.user'),
        ),
    ]
