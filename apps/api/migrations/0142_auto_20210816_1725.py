# Generated by Django 3.2.6 on 2021-08-16 17:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0141_auto_20210816_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('df971f2e-31c0-4986-b510-d8d35fbc090b'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('8fc88941-ee8d-4888-af78-0515af3e873a'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('f05c1a3c-14ed-45bc-b4ce-74ac51439e08'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('b823f86a-0808-4104-bf6a-b87b1b908ec1'), verbose_name='Slug'),
        ),
    ]