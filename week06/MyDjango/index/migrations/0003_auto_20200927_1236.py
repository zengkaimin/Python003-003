# Generated by Django 2.2.12 on 2020-09-27 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='name',
        ),
    ]
