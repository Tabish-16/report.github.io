# Generated by Django 4.2.4 on 2023-09-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0042_alter_gaseousemissionform_gaseem_reporting_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='gaseousemissionform',
            name='GaseEm_approved_by1',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
