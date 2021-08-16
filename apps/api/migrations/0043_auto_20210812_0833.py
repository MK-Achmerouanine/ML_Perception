# Generated by Django 3.2.6 on 2021-08-12 08:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_auto_20210811_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('1671d4f7-4e29-45f7-9d4e-842ddd32c834'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('bd291f18-e64a-4baa-b8a7-bedf9372c870'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('6bfbf394-dbe5-49d4-b013-cefaf1f0f1be'), verbose_name='Slug'),
        ),
    ]
