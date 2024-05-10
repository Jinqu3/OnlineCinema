# Generated by Django 5.0.3 on 2024-05-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0010_scorestar_alter_score_options_alter_score_star'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='name_en',
            field=models.CharField(max_length=56, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='country',
            name='name_ru',
            field=models.CharField(max_length=56, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='film',
            name='name_en',
            field=models.CharField(max_length=130, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='film',
            name='name_ru',
            field=models.CharField(max_length=130, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='film',
            name='slogan_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='slogan_ru',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_en',
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_ru',
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='member',
            name='gender_en',
            field=models.CharField(choices=[('Mужчина', 'Мужчина'), ('Женщина', 'Женщина')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='gender_ru',
            field=models.CharField(choices=[('Mужчина', 'Мужчина'), ('Женщина', 'Женщина')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='lastname_en',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='lastname_ru',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='name_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='name_ru',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='surname_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='surname_ru',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='name_en',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='name_ru',
            field=models.CharField(max_length=40, null=True),
        ),
    ]