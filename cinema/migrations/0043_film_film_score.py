# Generated by Django 5.0.3 on 2024-05-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0042_alter_film_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='film_score',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True),
        ),
    ]
