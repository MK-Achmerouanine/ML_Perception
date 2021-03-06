# Generated by Django 3.2.6 on 2021-08-11 13:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20210811_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('4938a902-f944-4432-854e-131266304e51'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('c9a1456f-6015-4760-9cd0-74622a1f0e55'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('3b1ec9a7-f477-4d1e-934a-7bccf9631d6a'), verbose_name='Slug'),
        ),
    ]
