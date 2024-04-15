# Generated by Django 5.0.3 on 2024-04-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_member_last_name_alter_film_name_alter_post_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'managed': True, 'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='favorite',
            options={'managed': True, 'verbose_name': 'Любимое'},
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'managed': True, 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'managed': True, 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'managed': True, 'verbose_name': 'Участник', 'verbose_name_plural': 'Участники'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'managed': True, 'verbose_name': 'Фото', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'managed': True, 'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'managed': True, 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'managed': True, 'verbose_name': 'Роль', 'verbose_name_plural': 'Роли'},
        ),
        migrations.AlterModelOptions(
            name='score',
            options={'managed': True, 'verbose_name': 'Оцененка', 'verbose_name_plural': 'Оценки'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True, 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='viewed',
            options={'managed': True, 'verbose_name': 'Просмотренное'},
        ),
        migrations.RenameField(
            model_name='film',
            old_name='reating',
            new_name='raiting',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='gedner',
            new_name='gender',
        ),
        migrations.AddField(
            model_name='film',
            name='trailer_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=56, unique=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/members/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(null=True, upload_to='media/photo/'),
        ),
    ]