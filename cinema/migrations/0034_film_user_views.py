# Generated by Django 5.0.3 on 2024-05-17 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0033_remove_user_roles_delete_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='user_views',
            field=models.ManyToManyField(blank=True, related_name='viewed', to='cinema.user'),
        ),
    ]
