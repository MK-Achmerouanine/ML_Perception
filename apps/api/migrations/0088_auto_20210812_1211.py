# Generated by Django 3.2.6 on 2021-08-12 12:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0087_auto_20210812_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('0ea87a0e-ed7c-44bb-aee6-10ffab646e0c'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('9a1a131f-94bc-4af2-956f-9f0cc06f35b3'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('9afa4560-bfc5-40e1-b5a4-1d7aba4dc385'), verbose_name='Slug'),
        ),
    ]
