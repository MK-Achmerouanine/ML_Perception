# Generated by Django 3.2.6 on 2021-08-18 11:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0172_auto_20210818_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('f22e9098-6baf-4e1e-bda1-f2a147961487'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('0777a387-c994-47d3-bce1-bfc62364d3cf'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('06d9b673-a787-44c6-adac-a06d6b58d075'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('78de5775-08a3-4416-8a81-b758d980f52f'), verbose_name='Slug'),
        ),
    ]
