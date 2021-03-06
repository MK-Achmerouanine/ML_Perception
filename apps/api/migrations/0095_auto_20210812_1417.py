# Generated by Django 3.2.6 on 2021-08-12 14:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0094_auto_20210812_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('34052f7a-9716-451c-8812-5c67ddf25cc6'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('23384e5f-6eb6-4c3d-b133-6b0db07e0bf0'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('3b849f18-2011-477f-a2a2-e07f432fe611'), verbose_name='Slug'),
        ),
    ]
