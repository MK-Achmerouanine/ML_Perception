# Generated by Django 3.2.6 on 2021-08-04 11:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_endpoint_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageToTranslate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.UUID('12e52c7b-217c-4569-83c8-6ef3eb72e4d7'), verbose_name='Slug')),
                ('image', models.ImageField(upload_to='images_to_translate', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
            ],
            options={
                'verbose_name': 'Image to translate',
                'verbose_name_plural': 'Images to translate',
            },
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('ab2d5ca9-77d5-4dda-b516-c3d27f794108'), null=True, verbose_name='Slug'),
        ),
    ]
