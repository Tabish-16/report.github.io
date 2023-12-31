# Generated by Django 4.2.4 on 2023-09-05 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0035_alter_drinkingwaterform_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambientair2',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ambientairform',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='drinkingwaterform',
            name='date_of_analysis_from',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='drinkingwaterform',
            name='date_of_analysis_to',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='drinkingwaterform',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='drinkingwaterform',
            name='reporting_date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='drinkingwaterform',
            name='sample_collection_date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='gaseousemissionform',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='luxanalysisform',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='machineoilform',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='noiseanalysis',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='packingpolybagform',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehiculemissionform',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='viscousliquid',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wastewaterform2',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wastewatersludge',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
