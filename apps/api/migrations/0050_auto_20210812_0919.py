# Generated by Django 3.2.6 on 2021-08-12 09:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_auto_20210812_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('6249c344-c9e9-43a2-b31d-08b34dbce093'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('f5c271a8-c078-4063-8b7d-c8336ca1d6cf'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('3f8bf8e3-40ef-4a77-8c71-23542c96f5b1'), verbose_name='Slug'),
        ),
    ]