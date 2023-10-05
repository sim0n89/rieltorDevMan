# Generated by Django 3.2 on 2023-10-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_rename_like_flat_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
