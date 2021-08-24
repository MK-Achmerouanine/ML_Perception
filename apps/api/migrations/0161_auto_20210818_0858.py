# Generated by Django 3.2.6 on 2021-08-18 08:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0160_auto_20210817_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('9b9c7b2b-4635-46da-a90e-88463c03c132'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('de9db5a1-be82-4fcf-8abc-ec0739297866'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('ad393a89-d04d-4584-bd56-854112809c19'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('f81e34b9-4e53-477b-86c7-895cd031a3f4'), verbose_name='Slug'),
        ),
    ]
