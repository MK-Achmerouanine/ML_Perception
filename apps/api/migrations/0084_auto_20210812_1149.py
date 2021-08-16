# Generated by Django 3.2.6 on 2021-08-12 11:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0083_auto_20210812_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('4d50d50a-d183-44b3-9800-739e09253ad0'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('ee4226ca-a8ac-4f5c-a73e-3b7d5b08b0b9'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('5efb92ab-8b76-4a28-a489-b582104fcf70'), verbose_name='Slug'),
        ),
    ]