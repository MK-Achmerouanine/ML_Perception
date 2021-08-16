# Generated by Django 3.2.6 on 2021-08-11 11:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210811_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextToAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.UUID('319a1a0d-c26a-4f11-b734-4f5e718ca890'), verbose_name='Slug')),
                ('audio', models.FileField(blank=True, null=True, upload_to='text_to_audio', verbose_name='Audio from text')),
                ('text', models.TextField(verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
            ],
            options={
                'verbose_name': 'Text to convert',
                'verbose_name_plural': 'Texts to convert',
            },
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('082251d0-7521-489e-b8d5-cf1fc4fbecb4'), null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='imagetotranslate',
            name='slug',
            field=models.SlugField(default=uuid.UUID('61aa1160-2275-44ea-8407-1a735ba08039'), verbose_name='Slug'),
        ),
    ]
