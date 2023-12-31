# Generated by Django 4.2.4 on 2023-09-01 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0026_luxanalysisform'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackingPolyBagForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_lab_rep_no', models.CharField(max_length=50)),
                ('pack_invoice', models.CharField(max_length=50)),
                ('pack_rep_date', models.CharField(max_length=50)),
                ('pack_rep_to', models.CharField(max_length=50)),
                ('pack_address', models.CharField(max_length=50)),
                ('pack_attention', models.CharField(max_length=50)),
                ('pack_email', models.CharField(max_length=50)),
                ('pack_sampleId', models.CharField(max_length=50)),
                ('pack_sample_colc_date', models.CharField(max_length=50)),
                ('pack_sample_desc', models.CharField(max_length=50)),
                ('pack_sample_type', models.CharField(max_length=50)),
                ('pack_sample_colc_by', models.CharField(max_length=50)),
                ('pack_test_desc', models.CharField(max_length=50)),
                ('pack_sr1', models.CharField(max_length=50)),
                ('pack_legend_1', models.CharField(max_length=50)),
                ('pack_legend_2', models.CharField(max_length=50)),
                ('pack_legend_3', models.CharField(max_length=50)),
                ('pack_legend_4', models.CharField(max_length=50)),
                ('pack_legend_5', models.CharField(max_length=50)),
                ('pack_legend_6', models.CharField(max_length=50)),
                ('pack_legend_7', models.CharField(max_length=50)),
                ('pack_legend_8', models.CharField(max_length=50)),
                ('pack_legend_9', models.CharField(max_length=50)),
                ('pack_legend_10', models.CharField(max_length=50)),
                ('pack_legend_11', models.CharField(max_length=50)),
                ('pack_legend_12', models.CharField(max_length=50)),
                ('pack_legend_13', models.CharField(max_length=50)),
                ('pack_legend_14', models.CharField(max_length=50)),
                ('pack_edit_note', models.CharField(max_length=50)),
                ('pack_custom_legend', models.CharField(max_length=50)),
                ('doc_con1', models.CharField(max_length=50)),
                ('doc_con2', models.CharField(max_length=50)),
                ('doc_con3', models.CharField(max_length=50)),
                ('pack_analyzed_by', models.ImageField(default='', upload_to='')),
                ('pack_reviewed_by', models.ImageField(default='', upload_to='')),
                ('pack_approved_by', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]
