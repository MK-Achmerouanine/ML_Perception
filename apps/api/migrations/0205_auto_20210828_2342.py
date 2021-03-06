# Generated by Django 3.2.6 on 2021-08-28 23:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0204_auto_20210828_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('0db8e5d0-b2da-4117-8554-e5d46965c598'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('7b89b44b-3cf6-4252-a041-207d8f4ae0a9'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('1b61c114-b4cf-44da-a416-9b3f2ef9111a'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('62c29f31-a6be-4219-9521-e72139bf0b7e'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('50a12d9e-547c-41cd-9051-97aad562a959'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttogcode',
            name='slug',
            field=models.SlugField(default=uuid.UUID('701e7278-bc23-49a6-9e39-fa00084e5133'), verbose_name='Slug'),
        ),
    ]
