# Generated by Django 4.2.4 on 2023-08-31 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0021_wastewatersludge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wastewatersludge',
            name='ww_sr14',
        ),
    ]
