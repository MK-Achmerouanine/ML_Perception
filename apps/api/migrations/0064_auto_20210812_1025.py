# Generated by Django 3.2.6 on 2021-08-12 10:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0063_auto_20210812_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('354dce62-222e-4476-a0cb-979b5bdda025'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('1b69e860-31e0-41af-8250-ac1dfdcea6d2'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('7ce9016d-3a33-4b8a-bf50-69238f673ecd'), verbose_name='Slug'),
        ),
    ]
