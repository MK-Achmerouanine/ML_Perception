# Generated by Django 3.2.6 on 2021-08-12 09:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_auto_20210812_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('7a3253bd-fd3c-4af5-865c-94d16249e7a3'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('193c928b-80dc-4568-9c27-8fc21b3f05ab'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('a50bda1b-a51b-44ef-b7d7-75c4bd1d763d'), verbose_name='Slug'),
        ),
    ]
