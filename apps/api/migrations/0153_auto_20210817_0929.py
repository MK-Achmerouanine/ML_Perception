# Generated by Django 3.2.6 on 2021-08-17 09:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0152_auto_20210817_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('bd0b80c1-9440-4301-9010-9c52893572c3'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('1c47de7f-f1b8-4686-8620-44a4ed6b97a0'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('428bedd3-654d-4414-8327-2319a763ae08'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('f9e6cb59-f55a-49e8-9896-b328201bdc41'), verbose_name='Slug'),
        ),
    ]
