# Generated by Django 3.2 on 2023-10-05 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_alter_owner_flats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]