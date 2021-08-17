# Generated by Django 3.2.6 on 2021-08-17 10:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0155_auto_20210817_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('9bcba368-10b9-4355-8b7c-2e5030408a68'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('e1b528af-6f00-4c6b-a502-19add56dea58'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('057d6046-26ba-48ee-8ecc-e4f90e021bde'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('befef9ea-e20f-4b3b-9ccc-055f9619777b'), verbose_name='Slug'),
        ),
    ]