# Generated by Django 3.2.6 on 2021-08-12 11:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0071_auto_20210812_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('a85fefc8-d50c-407b-b186-25214f58aed6'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('2900dd7a-1d42-4e53-832d-e600417b4555'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('618f3df5-1964-4e0b-b873-ab003a1860b7'), verbose_name='Slug'),
        ),
    ]
