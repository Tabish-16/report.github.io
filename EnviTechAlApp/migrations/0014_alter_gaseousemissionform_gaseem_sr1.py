# Generated by Django 4.2.4 on 2023-08-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0013_alter_gaseousemissionform_gaseem_sr1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gaseousemissionform',
            name='GaseEm_sr1',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
