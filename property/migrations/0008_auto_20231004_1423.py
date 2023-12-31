# Generated by Django 3.2 on 2023-10-04 11:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_alter_flat_has_balcony'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='has_balcony',
            field=models.NullBooleanField(db_index=True, verbose_name='Наличие балкона'),
        ),
    ]
