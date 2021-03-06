# Generated by Django 3.2.6 on 2021-08-13 15:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0129_auto_20210813_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('26dbd458-5e71-44fc-9b68-b62491fa6bc9'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('0530f9a5-943f-4064-a204-06d5a809e1ba'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('cff896eb-d469-484d-9488-c717e9781a17'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('cc500b44-2093-4d39-9166-2345b3457a03'), verbose_name='Slug'),
        ),
    ]
