# Generated by Django 4.2.4 on 2023-08-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0010_drinkingwaterform_analyzed_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkingwaterform',
            name='analyzed_by',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='drinkingwaterform',
            name='approved_by',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='drinkingwaterform',
            name='reviewed_by',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]