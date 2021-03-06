# Generated by Django 3.2.6 on 2021-08-18 14:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0175_auto_20210818_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('7898d3f8-c3b7-4700-b2d6-0ddb747fd289'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('c1a8d2e6-db07-4caf-b8f3-d90a54814a41'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('04855043-bdd4-42c7-b342-6dd9eac0fdac'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('622130e1-48ea-47de-bc5b-12197a56c547'), verbose_name='Slug'),
        ),
    ]
