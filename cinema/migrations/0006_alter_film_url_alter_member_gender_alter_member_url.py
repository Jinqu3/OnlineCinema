# Generated by Django 5.0.3 on 2024-05-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_member_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='url',
            field=models.SlugField(max_length=256, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('Mужчина', 'Мужчина'), ('Женщина', 'Женщина')], max_length=7),
        ),
        migrations.AlterField(
            model_name='member',
            name='url',
            field=models.SlugField(max_length=256, null=True, unique=True),
        ),
    ]
