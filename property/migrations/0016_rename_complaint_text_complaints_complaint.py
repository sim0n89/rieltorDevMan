# Generated by Django 3.2 on 2023-10-05 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_rename_owner_flats_owner_flats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaints',
            old_name='complaint_text',
            new_name='complaint',
        ),
    ]