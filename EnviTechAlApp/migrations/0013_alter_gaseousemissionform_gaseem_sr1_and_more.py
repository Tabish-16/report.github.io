# Generated by Django 4.2.4 on 2023-08-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0012_gaseousemissionform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gaseousemissionform',
            name='GaseEm_sr1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='gaseousemissionform',
            name='GaseEm_test_perf_date',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='gaseousemissionform',
            name='GaseEm_types',
            field=models.CharField(max_length=100),
        ),
    ]
