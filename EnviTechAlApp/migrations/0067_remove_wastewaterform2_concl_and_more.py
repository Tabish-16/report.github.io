# Generated by Django 4.2.4 on 2023-09-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0066_ambientair2_sr17_3_alter_ambientair2_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wastewaterform2',
            name='concl',
        ),
        migrations.RemoveField(
            model_name='wastewaterform2',
            name='legend_12',
        ),
        migrations.RemoveField(
            model_name='wastewaterform2',
            name='legend_13',
        ),
        migrations.RemoveField(
            model_name='wastewaterform2',
            name='legend_14',
        ),
        migrations.AddField(
            model_name='wastewaterform2',
            name='approvedby1',
            field=models.ImageField(max_length=50, null=True, upload_to=''),
        ),
    ]
