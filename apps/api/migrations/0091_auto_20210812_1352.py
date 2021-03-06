# Generated by Django 3.2.6 on 2021-08-12 13:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0090_auto_20210812_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('3a962f6b-f8b1-4871-be66-6a1f957e22d8'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('cc61c02b-3db6-4d2c-aa8e-b390d5500714'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('da30a645-7c47-484f-97a9-d3a00df5c817'), verbose_name='Slug'),
        ),
    ]
