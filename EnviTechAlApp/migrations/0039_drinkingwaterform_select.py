# Generated by Django 4.2.4 on 2023-09-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0038_remove_drinkingwaterform_conclusion'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinkingwaterform',
            name='select',
            field=models.CharField(max_length=50, null=True),
        ),
    ]