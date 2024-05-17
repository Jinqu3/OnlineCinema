# Generated by Django 5.0.3 on 2024-05-17 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0027_film_user_scores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
