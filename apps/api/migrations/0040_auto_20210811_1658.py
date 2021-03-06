# Generated by Django 3.2.6 on 2021-08-11 16:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_auto_20210811_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('59843083-8ab8-458f-bac2-66ab7a2db96f'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('2af8365b-e11c-4472-8e98-82b402d48831'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('8572ad7b-4637-4e98-8e6c-079f1579a7b6'), verbose_name='Slug'),
        ),
    ]
