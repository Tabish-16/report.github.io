# Generated by Django 4.2.4 on 2023-09-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0030_viscousliquid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmbientAir2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_rep_no', models.CharField(max_length=50)),
                ('invoice_no', models.CharField(max_length=50)),
                ('report_date', models.CharField(max_length=50)),
                ('report_to', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('attention', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('testId', models.CharField(max_length=50)),
                ('test_perf_date', models.CharField(max_length=50)),
                ('test_type', models.CharField(max_length=50)),
                ('test_desc', models.CharField(max_length=50)),
                ('test_test_perf_by', models.CharField(max_length=50)),
                ('sr1_1', models.CharField(max_length=50)),
                ('sr1_2', models.CharField(max_length=50)),
                ('sr1_3', models.CharField(max_length=50)),
                ('sr1_4', models.CharField(max_length=50)),
                ('sr1_5', models.CharField(max_length=50)),
                ('sr1_6', models.CharField(max_length=50)),
                ('sr1_7', models.CharField(max_length=50)),
                ('sr1_9', models.CharField(max_length=50)),
                ('sr1_10', models.CharField(max_length=50)),
                ('sr2_0', models.CharField(max_length=50)),
                ('sr2_1', models.CharField(max_length=50)),
                ('sr2_2', models.CharField(max_length=50)),
                ('sr2_3', models.CharField(max_length=50)),
                ('sr2_4', models.CharField(max_length=50)),
                ('sr2_5', models.CharField(max_length=50)),
                ('sr2_6', models.CharField(max_length=50)),
                ('sr2_7', models.CharField(max_length=50)),
                ('sr2_8', models.CharField(max_length=50)),
                ('sr2_9', models.CharField(max_length=50)),
                ('sr3_0', models.CharField(max_length=50)),
                ('sr3_1', models.CharField(max_length=50)),
                ('sr3_2', models.CharField(max_length=50)),
                ('sr3_3', models.CharField(max_length=50)),
                ('sr3_4', models.CharField(max_length=50)),
                ('sr3_5', models.CharField(max_length=50)),
                ('sr3_6', models.CharField(max_length=50)),
                ('sr3_7', models.CharField(max_length=50)),
                ('sr3_8', models.CharField(max_length=50)),
                ('sr3_9', models.CharField(max_length=50)),
                ('sr4_0', models.CharField(max_length=50)),
                ('sr4_1', models.CharField(max_length=50)),
                ('sr4_2', models.CharField(max_length=50)),
                ('sr4_3', models.CharField(max_length=50)),
                ('sr4_4', models.CharField(max_length=50)),
                ('sr4_5', models.CharField(max_length=50)),
                ('sr4_6', models.CharField(max_length=50)),
                ('sr4_7', models.CharField(max_length=50)),
                ('sr4_8', models.CharField(max_length=50)),
                ('sr4_9', models.CharField(max_length=50)),
                ('sr5_0', models.CharField(max_length=50)),
                ('sr5_1', models.CharField(max_length=50)),
                ('sr5_2', models.CharField(max_length=50)),
                ('sr5_3', models.CharField(max_length=50)),
                ('sr5_4', models.CharField(max_length=50)),
                ('sr5_5', models.CharField(max_length=50)),
                ('sr5_6', models.CharField(max_length=50)),
                ('sr5_7', models.CharField(max_length=50)),
                ('sr5_8', models.CharField(max_length=50)),
                ('sr5_9', models.CharField(max_length=50)),
                ('sr6_0', models.CharField(max_length=50)),
                ('sr6_1', models.CharField(max_length=50)),
                ('sr6_2', models.CharField(max_length=50)),
                ('sr6_3', models.CharField(max_length=50)),
                ('sr6_4', models.CharField(max_length=50)),
                ('sr6_5', models.CharField(max_length=50)),
                ('sr6_6', models.CharField(max_length=50)),
                ('sr6_7', models.CharField(max_length=50)),
                ('sr6_8', models.CharField(max_length=50)),
                ('sr6_9', models.CharField(max_length=50)),
                ('sr7_0', models.CharField(max_length=50)),
                ('sr7_1', models.CharField(max_length=50)),
                ('sr7_2', models.CharField(max_length=50)),
                ('sr7_3', models.CharField(max_length=50)),
                ('sr7_4', models.CharField(max_length=50)),
                ('sr7_5', models.CharField(max_length=50)),
                ('sr7_6', models.CharField(max_length=50)),
                ('sr7_7', models.CharField(max_length=50)),
                ('sr7_8', models.CharField(max_length=50)),
                ('sr7_9', models.CharField(max_length=50)),
                ('sr8_0', models.CharField(max_length=50)),
                ('sr8_1', models.CharField(max_length=50)),
                ('sr8_2', models.CharField(max_length=50)),
                ('sr8_3', models.CharField(max_length=50)),
                ('sr8_4', models.CharField(max_length=50)),
                ('sr8_5', models.CharField(max_length=50)),
                ('sr8_6', models.CharField(max_length=50)),
                ('sr8_7', models.CharField(max_length=50)),
                ('sr8_8', models.CharField(max_length=50)),
                ('sr8_9', models.CharField(max_length=50)),
                ('sr9_0', models.CharField(max_length=50)),
                ('sr9_1', models.CharField(max_length=50)),
                ('sr9_2', models.CharField(max_length=50)),
                ('sr9_3', models.CharField(max_length=50)),
                ('sr9_4', models.CharField(max_length=50)),
                ('sr9_5', models.CharField(max_length=50)),
                ('sr9_6', models.CharField(max_length=50)),
                ('sr9_7', models.CharField(max_length=50)),
                ('sr9_8', models.CharField(max_length=50)),
                ('sr9_9', models.CharField(max_length=50)),
                ('sr10_0', models.CharField(max_length=50)),
                ('sr10_1', models.CharField(max_length=50)),
                ('sr10_2', models.CharField(max_length=50)),
                ('sr10_3', models.CharField(max_length=50)),
                ('sr10_4', models.CharField(max_length=50)),
                ('sr10_5', models.CharField(max_length=50)),
                ('sr10_6', models.CharField(max_length=50)),
                ('sr10_7', models.CharField(max_length=50)),
                ('sr10_8', models.CharField(max_length=50)),
                ('sr10_9', models.CharField(max_length=50)),
                ('sr10_10', models.CharField(max_length=50)),
                ('sr11_0', models.CharField(max_length=50)),
                ('sr11_1', models.CharField(max_length=50)),
                ('sr11_2', models.CharField(max_length=50)),
                ('sr11_3', models.CharField(max_length=50)),
                ('sr11_4', models.CharField(max_length=50)),
                ('sr11_5', models.CharField(max_length=50)),
                ('sr11_6', models.CharField(max_length=50)),
                ('sr11_7', models.CharField(max_length=50)),
                ('sr11_8', models.CharField(max_length=50)),
                ('sr11_9', models.CharField(max_length=50)),
                ('sr12_0', models.CharField(max_length=50)),
                ('sr12_1', models.CharField(max_length=50)),
                ('sr12_2', models.CharField(max_length=50)),
                ('sr12_3', models.CharField(max_length=50)),
                ('sr12_4', models.CharField(max_length=50)),
                ('sr12_5', models.CharField(max_length=50)),
                ('sr12_6', models.CharField(max_length=50)),
                ('sr12_7', models.CharField(max_length=50)),
                ('sr12_8', models.CharField(max_length=50)),
                ('sr12_9', models.CharField(max_length=50)),
                ('sr13_0', models.CharField(max_length=50)),
                ('sr13_1', models.CharField(max_length=50)),
                ('sr13_2', models.CharField(max_length=50)),
                ('sr13_3', models.CharField(max_length=50)),
                ('sr13_4', models.CharField(max_length=50)),
                ('sr13_5', models.CharField(max_length=50)),
                ('sr13_6', models.CharField(max_length=50)),
                ('sr13_7', models.CharField(max_length=50)),
                ('sr13_8', models.CharField(max_length=50)),
                ('sr13_9', models.CharField(max_length=50)),
                ('sr14_0', models.CharField(max_length=50)),
                ('sr14_1', models.CharField(max_length=50)),
                ('sr14_2', models.CharField(max_length=50)),
                ('sr14_3', models.CharField(max_length=50)),
                ('sr14_4', models.CharField(max_length=50)),
                ('sr14_5', models.CharField(max_length=50)),
                ('sr14_6', models.CharField(max_length=50)),
                ('sr14_7', models.CharField(max_length=50)),
                ('sr14_8', models.CharField(max_length=50)),
                ('sr14_9', models.CharField(max_length=50)),
                ('sr15_0', models.CharField(max_length=50)),
                ('sr15_1', models.CharField(max_length=50)),
                ('sr15_2', models.CharField(max_length=50)),
                ('sr15_3', models.CharField(max_length=50)),
                ('sr15_4', models.CharField(max_length=50)),
                ('sr15_5', models.CharField(max_length=50)),
                ('sr15_6', models.CharField(max_length=50)),
                ('sr15_7', models.CharField(max_length=50)),
                ('sr15_8', models.CharField(max_length=50)),
                ('sr15_9', models.CharField(max_length=50)),
                ('sr16_0', models.CharField(max_length=50)),
                ('sr16_1', models.CharField(max_length=50)),
                ('sr16_2', models.CharField(max_length=50)),
                ('sr16_3', models.CharField(max_length=50)),
                ('sr16_4', models.CharField(max_length=50)),
                ('sr16_5', models.CharField(max_length=50)),
                ('sr16_6', models.CharField(max_length=50)),
                ('sr16_7', models.CharField(max_length=50)),
                ('sr16_8', models.CharField(max_length=50)),
                ('sr16_9', models.CharField(max_length=50)),
                ('sr17_0', models.CharField(max_length=50)),
                ('sr17_1', models.CharField(max_length=50)),
                ('sr17_2', models.CharField(max_length=50)),
                ('sr17_4', models.CharField(max_length=50)),
                ('sr17_5', models.CharField(max_length=50)),
                ('sr17_6', models.CharField(max_length=50)),
                ('sr17_7', models.CharField(max_length=50)),
                ('sr17_8', models.CharField(max_length=50)),
                ('sr17_9', models.CharField(max_length=50)),
                ('sr18_0', models.CharField(max_length=50)),
                ('sr18_1', models.CharField(max_length=50)),
                ('sr18_2', models.CharField(max_length=50)),
                ('sr18_3', models.CharField(max_length=50)),
                ('sr18_4', models.CharField(max_length=50)),
                ('sr18_5', models.CharField(max_length=50)),
                ('sr18_6', models.CharField(max_length=50)),
                ('sr18_7', models.CharField(max_length=50)),
                ('sr18_8', models.CharField(max_length=50)),
                ('sr18_9', models.CharField(max_length=50)),
                ('sr19_0', models.CharField(max_length=50)),
                ('sr19_1', models.CharField(max_length=50)),
                ('sr19_2', models.CharField(max_length=50)),
                ('sr19_3', models.CharField(max_length=50)),
                ('sr19_4', models.CharField(max_length=50)),
                ('sr19_5', models.CharField(max_length=50)),
                ('sr19_6', models.CharField(max_length=50)),
                ('sr19_7', models.CharField(max_length=50)),
                ('sr19_8', models.CharField(max_length=50)),
                ('sr19_9', models.CharField(max_length=50)),
                ('sr20_0', models.CharField(max_length=50)),
                ('sr20_1', models.CharField(max_length=50)),
                ('sr20_2', models.CharField(max_length=50)),
                ('sr20_3', models.CharField(max_length=50)),
                ('sr20_4', models.CharField(max_length=50)),
                ('sr20_5', models.CharField(max_length=50)),
                ('sr20_6', models.CharField(max_length=50)),
                ('sr20_7', models.CharField(max_length=50)),
                ('sr20_8', models.CharField(max_length=50)),
                ('sr20_9', models.CharField(max_length=50)),
                ('sr21_0', models.CharField(max_length=50)),
                ('sr21_1', models.CharField(max_length=50)),
                ('sr21_2', models.CharField(max_length=50)),
                ('sr21_3', models.CharField(max_length=50)),
                ('sr21_4', models.CharField(max_length=50)),
                ('sr21_5', models.CharField(max_length=50)),
                ('sr21_6', models.CharField(max_length=50)),
                ('sr21_7', models.CharField(max_length=50)),
                ('sr21_8', models.CharField(max_length=50)),
                ('sr21_9', models.CharField(max_length=50)),
                ('sr22_0', models.CharField(max_length=50)),
                ('sr22_1', models.CharField(max_length=50)),
                ('sr22_2', models.CharField(max_length=50)),
                ('sr22_3', models.CharField(max_length=50)),
                ('sr22_4', models.CharField(max_length=50)),
                ('sr22_5', models.CharField(max_length=50)),
                ('sr22_6', models.CharField(max_length=50)),
                ('sr22_7', models.CharField(max_length=50)),
                ('sr22_8', models.CharField(max_length=50)),
                ('sr22_9', models.CharField(max_length=50)),
                ('sr23_0', models.CharField(max_length=50)),
                ('sr23_1', models.CharField(max_length=50)),
                ('sr23_2', models.CharField(max_length=50)),
                ('sr23_3', models.CharField(max_length=50)),
                ('sr23_4', models.CharField(max_length=50)),
                ('sr23_5', models.CharField(max_length=50)),
                ('sr23_6', models.CharField(max_length=50)),
                ('sr23_7', models.CharField(max_length=50)),
                ('sr23_8', models.CharField(max_length=50)),
                ('sr23_9', models.CharField(max_length=50)),
                ('sr24_0', models.CharField(max_length=50)),
                ('sr24_1', models.CharField(max_length=50)),
                ('sr24_2', models.CharField(max_length=50)),
                ('sr24_3', models.CharField(max_length=50)),
                ('sr24_4', models.CharField(max_length=50)),
                ('sr24_5', models.CharField(max_length=50)),
                ('sr24_6', models.CharField(max_length=50)),
                ('sr24_7', models.CharField(max_length=50)),
                ('sr24_8', models.CharField(max_length=50)),
                ('sr24_9', models.CharField(max_length=50)),
                ('sr25_0', models.CharField(max_length=50)),
                ('sr25_1', models.CharField(max_length=50)),
                ('sr25_2', models.CharField(max_length=50)),
                ('sr25_3', models.CharField(max_length=50)),
                ('sr25_4', models.CharField(max_length=50)),
                ('sr25_5', models.CharField(max_length=50)),
                ('sr25_6', models.CharField(max_length=50)),
                ('sr25_7', models.CharField(max_length=50)),
                ('sr25_8', models.CharField(max_length=50)),
                ('select', models.CharField(max_length=50)),
                ('concl', models.CharField(max_length=50)),
                ('legend_1', models.CharField(max_length=50)),
                ('legend_2', models.CharField(max_length=50)),
                ('legend_3', models.CharField(max_length=50)),
                ('legend_4', models.CharField(max_length=50)),
                ('legend_5', models.CharField(max_length=50)),
                ('legend_6', models.CharField(max_length=50)),
                ('legend_7', models.CharField(max_length=50)),
                ('legend_8', models.CharField(max_length=50)),
                ('legend_9', models.CharField(max_length=50)),
                ('legend_10', models.CharField(max_length=50)),
                ('legend_11', models.CharField(max_length=50)),
                ('legend_12', models.CharField(max_length=50)),
                ('legend_13', models.CharField(max_length=50)),
                ('legend_14', models.CharField(max_length=50)),
                ('edit_note', models.CharField(max_length=50)),
                ('custom_legend', models.CharField(max_length=50)),
                ('doc1', models.CharField(max_length=50)),
                ('doc2', models.CharField(max_length=50)),
                ('doc3', models.CharField(max_length=50)),
                ('analyzedby', models.ImageField(max_length=50, upload_to='')),
                ('reviewedby', models.ImageField(max_length=50, upload_to='')),
                ('approvedby', models.ImageField(max_length=50, upload_to='')),
            ],
        ),
    ]
