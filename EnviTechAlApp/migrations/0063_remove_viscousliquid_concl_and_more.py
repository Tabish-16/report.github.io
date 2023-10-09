# Generated by Django 4.2.4 on 2023-09-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0062_remove_microbialanalysis_micro_concl_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viscousliquid',
            name='concl',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_10',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_11',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_12',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_13',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_14',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_3',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_4',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_5',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_6',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_7',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_8',
        ),
        migrations.RemoveField(
            model_name='viscousliquid',
            name='legend_9',
        ),
        migrations.AddField(
            model_name='viscousliquid',
            name='approvedby1',
            field=models.ImageField(max_length=50, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_attention',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_custom_legend',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_date_analysis',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_doc1',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_doc2',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_doc3',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_editnote',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_email',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_invoice_bill',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_lab_report_no',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_legend_1',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_legend_2',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_rep_date',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_rep_to',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_sampleId',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_sample_col_by',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_sample_col_date',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_sample_desc',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_sample_type',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_sr1',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_sr2',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_sr3',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_sr4',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_sr5',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_sr6',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microbialanalysis',
            name='micro_test_desc',
            field=models.CharField(max_length=150),
        ),
    ]
