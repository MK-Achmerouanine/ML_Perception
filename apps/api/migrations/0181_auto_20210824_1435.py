# Generated by Django 3.2.6 on 2021-08-24 14:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0180_auto_20210824_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('769e12a2-649b-496a-8386-979853555c97'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('e370d5ae-8495-4c63-be7c-6fe2723d7652'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('0e173bbf-55c9-4f5c-8deb-32f49b854016'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('85fe12c0-d7a9-49b2-aebb-66033b855a8b'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('70ea3df1-656a-4182-90a1-a80d99c79199'), verbose_name='Slug'),
        ),
    ]