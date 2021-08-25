# Generated by Django 3.2.6 on 2021-08-24 16:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0187_auto_20210824_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('180a2026-35b5-417f-9ef9-c0935b55367a'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('c0421ad2-679e-4ba1-831b-7ae8e90b5498'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('ed2b6466-0dd2-4a6a-bfb8-bfcee4a5ffa9'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('db75a442-a87a-46fc-b1ec-efbc723ce961'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('fb7b1c97-00a1-43a6-82dc-4190053e5c54'), verbose_name='Slug'),
        ),
    ]
