# Generated by Django 5.0.3 on 2024-05-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0034_film_user_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='user_favorite',
            field=models.ManyToManyField(blank=True, related_name='film_favorites', to='cinema.user'),
        ),
        migrations.AlterField(
            model_name='film',
            name='user_views',
            field=models.ManyToManyField(blank=True, related_name='film_viewed', to='cinema.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('Mужчина', 'Мужчина'), ('Женщина', 'Женщина'), ('Man', 'Man'), ('Woman', 'Woman')], max_length=7, null=True),
        ),
    ]
