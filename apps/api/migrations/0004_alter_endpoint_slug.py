# Generated by Django 3.2.6 on 2021-08-04 10:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210804_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('f00a2923-ee0c-43f7-9cd0-035bb424e6b9'), null=True, verbose_name='Slug'),
        ),
    ]
