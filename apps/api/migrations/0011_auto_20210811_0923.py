# Generated by Django 3.2.6 on 2021-08-11 09:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210809_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('c39f6d62-6df0-4342-8f50-af7eaa961ff2'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('e5bf4d6d-9d10-4455-80ac-b81d989253fa'), verbose_name='Slug'),
        ),
    ]