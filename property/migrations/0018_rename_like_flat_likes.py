# Generated by Django 3.2 on 2023-10-05 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20231005_0800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='like',
            new_name='likes',
        ),
    ]