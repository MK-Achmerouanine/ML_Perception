# Generated by Django 3.2.6 on 2021-08-12 11:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0086_auto_20210812_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('a1edf865-5c76-401f-a247-2bf88d7fec63'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('a723cdcf-11f7-4dcd-80b9-538df0a2d01f'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('18dac66c-1ad4-4a67-a416-8b7a27c76ad9'), verbose_name='Slug'),
        ),
    ]
