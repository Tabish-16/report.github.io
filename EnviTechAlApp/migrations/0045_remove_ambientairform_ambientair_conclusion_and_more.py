# Generated by Django 4.2.4 on 2023-09-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0044_gaseousemissionform_gaseem_select'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambientairform',
            name='ambientAir_conclusion',
        ),
        migrations.AlterField(
            model_name='gaseousemissionform',
            name='GaseEm_edit_note',
            field=models.CharField(max_length=500, null=True),
        ),
    ]