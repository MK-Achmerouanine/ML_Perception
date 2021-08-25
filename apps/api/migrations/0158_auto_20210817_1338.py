# Generated by Django 3.2.6 on 2021-08-17 13:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0157_auto_20210817_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('e82ead13-019f-4491-bb61-1a1b1bdd536b'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('95f0c9c1-a890-413e-acae-632efcfed0cc'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('e3a378c5-c075-41d7-8f14-49b8fda74450'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('02ae3cfe-5257-45ce-a798-30395c5bc8e4'), verbose_name='Slug'),
        ),
    ]