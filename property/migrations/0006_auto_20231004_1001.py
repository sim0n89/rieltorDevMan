# Generated by Django 2.2.24 on 2023-10-04 07:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_complaints'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaints',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='flat',
            options={'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AddField(
            model_name='flat',
            name='like',
            field=models.ManyToManyField(related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
