# Generated by Django 3.2.6 on 2021-08-13 15:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0131_auto_20210813_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('7ff79549-e495-470b-baf0-66946f2879a8'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('b6b14008-2813-468c-8ac0-7d06e07ec1cd'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('acc3e9bf-78fc-4887-9b1f-520429b5d5ca'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('bad783b4-8ce3-4476-a516-1222861ba2aa'), verbose_name='Slug'),
        ),
    ]
