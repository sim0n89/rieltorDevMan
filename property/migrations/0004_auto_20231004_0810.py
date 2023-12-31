# Generated by Django 2.2.24 on 2023-10-04 05:10

from django.db import migrations


def change_new_building_in_flat_table(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)
    for flat in Flat.objects.all():
        if flat.construction_year >= 2015:
            flat.new_building = True
        else:
            flat.new_building = False
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0003_flat_new_building"),
    ]

    operations = [
        migrations.RunPython(
            change_new_building_in_flat_table, migrations.RunPython.noop
        )
    ]
