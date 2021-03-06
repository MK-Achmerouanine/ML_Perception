# Generated by Django 3.2.6 on 2021-08-18 13:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0173_auto_20210818_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('710e85a4-ccf1-4bdd-8705-ab94de516ea7'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('df49e215-d287-46fb-9bf8-91cb845bc09b'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('94181f32-fe01-4b07-b178-2ba223d4e9a9'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('9bfa4230-4a8d-4423-b7b9-fea385d344df'), verbose_name='Slug'),
        ),
    ]
