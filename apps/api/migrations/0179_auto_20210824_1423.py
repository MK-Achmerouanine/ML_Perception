# Generated by Django 3.2.6 on 2021-08-24 14:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0178_auto_20210824_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('5c1aba8a-ae22-4f29-9ca6-de5c709c537f'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('33a288c5-de8c-4b68-8414-6c72a58e9f62'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('82bb5aeb-c3b7-4fcd-bbe1-11b64ca91fe8'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('71fb88a2-1b46-400b-82c6-90acb3fa175d'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('446df014-32c1-4961-9f1c-0c47d6a8cbaa'), verbose_name='Slug'),
        ),
    ]
