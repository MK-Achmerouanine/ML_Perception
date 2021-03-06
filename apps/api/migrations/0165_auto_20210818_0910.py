# Generated by Django 3.2.6 on 2021-08-18 09:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0164_auto_20210818_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('cbc01d03-48f2-4f03-a71d-04f1c07347e0'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('74139459-7863-404e-915b-57ce2a142b86'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('2ebe4378-67d8-4762-bf3a-bd55ab2916d3'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('c157caa7-89a4-4db0-a02b-733fefa0225b'), verbose_name='Slug'),
        ),
    ]
