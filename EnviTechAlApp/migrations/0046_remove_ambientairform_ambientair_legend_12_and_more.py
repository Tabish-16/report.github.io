# Generated by Django 4.2.4 on 2023-09-20 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0045_remove_ambientairform_ambientair_conclusion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambientairform',
            name='ambientAir_legend_12',
        ),
        migrations.RemoveField(
            model_name='ambientairform',
            name='ambientAir_legend_13',
        ),
        migrations.RemoveField(
            model_name='ambientairform',
            name='ambientAir_legend_14',
        ),
        migrations.AddField(
            model_name='ambientairform',
            name='ambientAir_approved_by1',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
    ]