# Generated by Django 4.2.4 on 2023-09-22 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0053_vehiculemissionform_vehem_edit_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculemissionform',
            name='vehEm_concl',
        ),
    ]
