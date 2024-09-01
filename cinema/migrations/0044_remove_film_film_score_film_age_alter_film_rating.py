# Generated by Django 5.0.3 on 2024-05-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0043_film_film_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='film_score',
        ),
        migrations.AddField(
            model_name='film',
            name='age',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True),
        ),
    ]