# Generated by Django 4.2.4 on 2023-09-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0058_remove_noiseanalysis_concl_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='noiseanalysis',
            name='select1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='noiseanalysis',
            name='select',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
