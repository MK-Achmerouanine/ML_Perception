# Generated by Django 3.2.6 on 2021-08-12 08:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_auto_20210812_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('7d4350e2-c8f6-4576-95e3-84a2de6ae8b9'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('a100f17a-d5db-4313-9063-11a81b009f3b'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('55465d5c-d594-4b18-bdd9-227b7b004be6'), verbose_name='Slug'),
        ),
    ]
