# Generated by Django 3.2.6 on 2021-08-11 15:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20210811_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('fda4b585-9987-44a0-a0ab-7f2ecc38137a'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('dff0821a-64cf-4c03-af19-5b473bfa42a2'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('37889025-37a4-424b-b843-8f2f366a7cd9'), verbose_name='Slug'),
        ),
    ]
