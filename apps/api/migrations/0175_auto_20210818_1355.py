# Generated by Django 3.2.6 on 2021-08-18 13:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0174_auto_20210818_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('d29047f9-3d28-48e1-b0e2-1fcdb91ad82d'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('41ab72fe-2211-446e-bba5-786125020576'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('6b3f7be5-049b-4667-8e7c-517852588067'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('36ecdb26-15c7-422f-b9c4-49905e6170f1'), verbose_name='Slug'),
        ),
    ]
