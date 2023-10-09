# Generated by Django 4.2.4 on 2023-09-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0025_rename_venem_sr1_vehiculemissionform_vehem_sr1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LuxAnalysisForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lux_lab_report_no', models.CharField(max_length=50)),
                ('lux_invoice_no', models.CharField(max_length=50)),
                ('lux_report_date', models.CharField(max_length=50)),
                ('lux_report_to', models.CharField(max_length=50)),
                ('lux_address', models.CharField(max_length=50)),
                ('lux_attention', models.CharField(max_length=50)),
                ('lux_email', models.CharField(max_length=50)),
                ('lux_testId', models.CharField(max_length=50)),
                ('lux_test_perf_date', models.CharField(max_length=50)),
                ('lux_test_type', models.CharField(max_length=50)),
                ('lux_test_perfBy', models.CharField(max_length=50)),
                ('lux_test_desc', models.CharField(max_length=50)),
                ('lux_parameters_1', models.CharField(max_length=50)),
                ('lux_result_1', models.CharField(max_length=50)),
                ('lux_parameters_2', models.CharField(max_length=50)),
                ('lux_result_2', models.CharField(max_length=50)),
                ('lux_parameters_3', models.CharField(max_length=50)),
                ('lux_result_3', models.CharField(max_length=50)),
                ('lux_parameters_4', models.CharField(max_length=50)),
                ('lux_result_4', models.CharField(max_length=50)),
                ('lux_parameters_5', models.CharField(max_length=50)),
                ('lux_result_5', models.CharField(max_length=50)),
                ('lux_parameters_6', models.CharField(max_length=50)),
                ('lux_result_6', models.CharField(max_length=50)),
                ('lux_parameters_7', models.CharField(max_length=50)),
                ('lux_result_7', models.CharField(max_length=50)),
                ('lux_parameters_8', models.CharField(max_length=50)),
                ('lux_result_8', models.CharField(max_length=50)),
                ('lux_parameters_9', models.CharField(max_length=50)),
                ('lux_result_9', models.CharField(max_length=50)),
                ('lux_parameters_10', models.CharField(max_length=50)),
                ('lux_result_10', models.CharField(max_length=50)),
                ('lux_parameters_11', models.CharField(max_length=50)),
                ('lux_result_11', models.CharField(max_length=50)),
                ('lux_parameters_12', models.CharField(max_length=50)),
                ('lux_result_12', models.CharField(max_length=50)),
                ('lux_parameters_13', models.CharField(max_length=50)),
                ('lux_result_13', models.CharField(max_length=50)),
                ('lux_concl', models.CharField(max_length=50)),
                ('lux_legend_1', models.CharField(max_length=50)),
                ('lux_legend_2', models.CharField(max_length=50)),
                ('lux_legend_3', models.CharField(max_length=50)),
                ('lux_legend_4', models.CharField(max_length=50)),
                ('lux_legend_5', models.CharField(max_length=50)),
                ('lux_legend_6', models.CharField(max_length=50)),
                ('lux_legend_7', models.CharField(max_length=50)),
                ('lux_legend_8', models.CharField(max_length=50)),
                ('lux_legend_9', models.CharField(max_length=50)),
                ('lux_legend_10', models.CharField(max_length=50)),
                ('lux_legend_11', models.CharField(max_length=50)),
                ('lux_legend_12', models.CharField(max_length=50)),
                ('lux_legend_13', models.CharField(max_length=50)),
                ('lux_legend_14', models.CharField(max_length=50)),
                ('lux_edit_note', models.CharField(max_length=50)),
                ('lux_custom_legend', models.CharField(max_length=50)),
                ('lux_doc_con1', models.CharField(max_length=50)),
                ('lux_doc_con2', models.CharField(max_length=50)),
                ('lux_doc_con3', models.CharField(max_length=50)),
                ('lux_analyzedby', models.ImageField(default='', upload_to='')),
                ('lux_reviewedby', models.ImageField(default='', upload_to='')),
                ('lux_approvedby', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]