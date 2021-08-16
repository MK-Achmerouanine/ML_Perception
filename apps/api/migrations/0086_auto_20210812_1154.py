# Generated by Django 3.2.6 on 2021-08-12 11:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0085_auto_20210812_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('7f65a902-ac05-4b0f-9e00-540e9f0574a4'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('b5b43cce-6678-4f8b-a492-5d4c0e5528c0'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('be3a3adb-f9f0-4504-8924-37f350ff2a21'), verbose_name='Slug'),
        ),
    ]