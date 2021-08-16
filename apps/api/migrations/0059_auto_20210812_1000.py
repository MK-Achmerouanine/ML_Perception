# Generated by Django 3.2.6 on 2021-08-12 10:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0058_auto_20210812_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('f7700455-72c2-4f97-8edf-770bbb069f29'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('9d6be4c1-ad8c-4914-95f9-bf9f5329964e'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('b69ecc0a-e165-43ec-a528-e6a0fc9ead78'), verbose_name='Slug'),
        ),
    ]
