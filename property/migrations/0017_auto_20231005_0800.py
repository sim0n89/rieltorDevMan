# Generated by Django 3.2 on 2023-10-05 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0016_rename_complaint_text_complaints_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='Автор жалобы'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.flat', verbose_name='Квартира'),
        ),
    ]
