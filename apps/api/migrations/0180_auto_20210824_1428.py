# Generated by Django 3.2.6 on 2021-08-24 14:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0179_auto_20210824_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('436458b9-4c97-4604-a433-392d986583ed'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('37c40edf-d40a-49d6-9dbb-ef5b554db059'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetoaudio',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='text_to_audio', verbose_name='Audio'),
        ),
        migrations.AlterField(
            model_name='imagetoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('abb9a191-5fb3-4d8a-b270-1975fb2d69cc'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('52c9c786-db1f-4e1c-9a9b-1e42441a653d'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('5293ace7-e5b2-476f-8142-5add8bab771e'), verbose_name='Slug'),
        ),
    ]
