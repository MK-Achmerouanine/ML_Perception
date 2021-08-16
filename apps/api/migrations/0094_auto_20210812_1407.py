# Generated by Django 3.2.6 on 2021-08-12 14:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0093_auto_20210812_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('7774832e-7ec1-4135-91a3-f2373d17999e'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('7c8f569e-90b7-4be4-9ef1-3a3772293884'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('65955823-629e-4655-9941-6af4a6655e5c'), verbose_name='Slug'),
        ),
    ]