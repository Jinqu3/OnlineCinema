# Generated by Django 5.0.3 on 2024-05-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_alter_film_description_alter_member_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='url',
            field=models.SlugField(blank=True, max_length=256, null=True, unique=True),
        ),
    ]