# Generated by Django 2.2.7 on 2019-11-16 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_personalblog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalblog',
            old_name='user',
            new_name='author',
        ),
    ]
