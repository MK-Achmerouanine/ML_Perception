# Generated by Django 3.2.6 on 2021-08-28 23:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0202_auto_20210828_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('e4692413-9761-422f-a78f-a68e0f19fa67'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('6d112221-a8ab-4608-b0e7-f55ae60b031e'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('7c82ab0e-cbea-434c-b434-c148640d7a53'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('74a73321-2d55-433d-920e-bc15abb33412'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('2ed1a698-4908-4312-9369-4299eb4c6d56'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttogcode',
            name='slug',
            field=models.SlugField(default=uuid.UUID('f916d0b2-1ae3-4ae0-81fe-0c5a9b06ae96'), verbose_name='Slug'),
        ),
    ]
