# Generated by Django 3.2.6 on 2021-08-24 14:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0184_auto_20210824_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('1422155a-0174-444c-aa8b-66c16894e7fc'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('8104d1d6-1f78-497b-ad9f-17cb32be2735'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('bc233bc2-935b-4631-8e04-46cd927aeac2'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('aacd774e-f1a9-433b-a731-31fcc44774d0'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('864027d7-52dd-4201-af79-fa0313262a2a'), verbose_name='Slug'),
        ),
    ]
