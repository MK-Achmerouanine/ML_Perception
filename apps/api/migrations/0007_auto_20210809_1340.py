# Generated by Django 3.2.6 on 2021-08-09 13:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210804_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagetotranslate',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('93486ee9-4f71-4ef1-8b1f-3c78f0ab034e'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('b4ef4310-6034-4510-a08d-11a0bded86f8'), verbose_name='Slug'),
        ),
    ]