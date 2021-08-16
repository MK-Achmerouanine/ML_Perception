# Generated by Django 3.2.6 on 2021-08-13 09:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0119_auto_20210813_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('3794ca2a-e084-4eb2-ba11-0aaa71d55b4c'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('fe401718-3fac-4ff3-8561-1106e0bebf1b'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('f7466521-ae25-43f0-b623-562c3f5ea2a9'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('0a2e0fc4-67a8-430a-bb7d-ae2b28fae2dc'), verbose_name='Slug'),
        ),
    ]
