# Generated by Django 3.2.6 on 2021-08-04 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endpoint',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
