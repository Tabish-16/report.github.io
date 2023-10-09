# Generated by Django 4.2.4 on 2023-09-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0033_wastewaterform2'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoiseAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_rep_no', models.CharField(max_length=50)),
                ('invoice_no', models.CharField(max_length=50)),
                ('rep_date', models.CharField(max_length=50)),
                ('report_to', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('attention', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('testId', models.CharField(max_length=50)),
                ('test_perf_date', models.CharField(max_length=50)),
                ('test_type', models.CharField(max_length=50)),
                ('test_perf_by', models.CharField(max_length=50)),
                ('test_desc', models.CharField(max_length=50)),
                ('select', models.CharField(max_length=50)),
                ('r1', models.CharField(max_length=50)),
                ('r1_1', models.CharField(max_length=50)),
                ('r2', models.CharField(max_length=50)),
                ('r2_2', models.CharField(max_length=50)),
                ('r3', models.CharField(max_length=50)),
                ('r3_3', models.CharField(max_length=50)),
                ('r4', models.CharField(max_length=50)),
                ('r4_4', models.CharField(max_length=50)),
                ('r5', models.CharField(max_length=50)),
                ('r5_5', models.CharField(max_length=50)),
                ('r6', models.CharField(max_length=50)),
                ('r6_6', models.CharField(max_length=50)),
                ('r7', models.CharField(max_length=50)),
                ('r7_7', models.CharField(max_length=50)),
                ('r8', models.CharField(max_length=50)),
                ('r8_8', models.CharField(max_length=50)),
                ('r9', models.CharField(max_length=50)),
                ('r9_9', models.CharField(max_length=50)),
                ('r10', models.CharField(max_length=50)),
                ('r10_10', models.CharField(max_length=50)),
                ('r11', models.CharField(max_length=50)),
                ('r11_11', models.CharField(max_length=50)),
                ('r12', models.CharField(max_length=50)),
                ('r12_12', models.CharField(max_length=50)),
                ('r13', models.CharField(max_length=50)),
                ('r13_13', models.CharField(max_length=50)),
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
                ('editNote', models.CharField(max_length=50)),
                ('customlegend', models.CharField(max_length=50)),
                ('doc1', models.CharField(max_length=50)),
                ('doc2', models.CharField(max_length=50)),
                ('doc3', models.CharField(max_length=50)),
                ('analyzedby', models.ImageField(max_length=50, upload_to='')),
                ('reviewedby', models.ImageField(max_length=50, upload_to='')),
                ('approvedby', models.ImageField(max_length=50, upload_to='')),
            ],
        ),
    ]