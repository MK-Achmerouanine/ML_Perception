# Generated by Django 3.2.6 on 2021-08-12 10:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0064_auto_20210812_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('eb737d46-7a73-4c8d-927f-c28c8c4097a7'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('b63c61f7-7253-424d-a076-9cc22ff7e89a'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('e1ebd247-cc47-4b92-bf47-f3cd0cbd679e'), verbose_name='Slug'),
        ),
    ]
