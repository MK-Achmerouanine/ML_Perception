# Generated by Django 3.2.6 on 2021-08-13 09:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0120_auto_20210813_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiototext',
            name='slug',
            field=models.SlugField(default=uuid.UUID('e628ff17-6b1a-4fec-b51b-970cefc7f370'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('b0493cc8-02be-4728-8467-59033ac44c5f'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('e2f247d0-0299-4bba-be90-ea9c625d0fb5'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='texttoaudio',
            name='slug',
            field=models.SlugField(default=uuid.UUID('f27fb2b9-ae57-4508-b57f-52eea169eef1'), verbose_name='Slug'),
        ),
    ]
