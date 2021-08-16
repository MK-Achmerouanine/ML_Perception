# Generated by Django 3.2.6 on 2021-08-11 15:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20210811_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('fc69365d-0750-4e0a-b69b-645a6a3ee692'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('024c56e0-97d6-402d-b5e5-4f5ca3c35728'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('3e008bd1-63bc-4c1a-af93-ede99a21612c'), verbose_name='Slug'),
        ),
    ]
