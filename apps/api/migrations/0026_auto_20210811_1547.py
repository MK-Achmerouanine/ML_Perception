# Generated by Django 3.2.6 on 2021-08-11 15:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20210811_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('bfd6e7d2-14e4-434c-b341-45d0d6f7834b'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('45470d1d-6a7b-41fa-87e7-2693ab191581'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('48defde2-a509-44c2-95a7-928d899beab4'), verbose_name='Slug'),
        ),
    ]
