# Generated by Django 3.2.6 on 2021-08-13 10:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0124_auto_20210813_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('f08f9154-0b8b-4642-8959-5b0488d53e35'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('99a0755d-8bd7-43e7-af5d-6a1080fb878c'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('c74c9bca-4f01-4949-8f06-a314789044a9'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('c3ec4acc-52ac-4d79-8c0c-775d6e25cc38'), verbose_name='Slug'),
        ),
    ]
