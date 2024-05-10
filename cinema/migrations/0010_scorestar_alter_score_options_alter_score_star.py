# Generated by Django 5.0.3 on 2024-05-10 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0009_alter_member_members_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
            ],
            options={
                'verbose_name': 'Звезда оценки',
                'verbose_name_plural': 'Звезды',
                'ordering': ['-value'],
            },
        ),
        migrations.AlterModelOptions(
            name='score',
            options={'managed': True, 'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
        migrations.AlterField(
            model_name='score',
            name='star',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.scorestar'),
        ),
    ]
