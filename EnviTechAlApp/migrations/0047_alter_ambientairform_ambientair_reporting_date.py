# Generated by Django 4.2.4 on 2023-09-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0046_remove_ambientairform_ambientair_legend_12_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambientairform',
            name='ambientAir_reporting_date',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
