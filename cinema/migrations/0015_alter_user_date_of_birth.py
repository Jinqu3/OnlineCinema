# Generated by Django 5.0.3 on 2024-05-13 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0014_user_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]