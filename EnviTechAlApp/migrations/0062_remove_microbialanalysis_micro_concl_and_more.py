# Generated by Django 4.2.4 on 2023-09-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnviTechAlApp', '0061_remove_machineoilform_machine_conl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_concl',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_10',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_11',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_12',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_13',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_14',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_3',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_4',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_5',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_6',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_7',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_8',
        ),
        migrations.RemoveField(
            model_name='microbialanalysis',
            name='micro_legend_9',
        ),
        migrations.AddField(
            model_name='microbialanalysis',
            name='micro_approvedby1',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
    ]
