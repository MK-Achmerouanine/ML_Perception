# Generated by Django 3.2.6 on 2021-08-16 21:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0146_auto_20210816_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('e1c63c6d-f9c0-435d-aac9-2fe899dd27e5'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('1228bdc6-3a1f-4941-8196-906c1094971c'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('c340063b-e44c-48df-af66-99c023f41aff'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('aa473c5c-d2a0-4c0e-a429-b67928b9d2fa'), verbose_name='Slug'),
        ),
    ]
