# Generated by Django 2.0.5 on 2018-07-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0013_auto_20180705_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='numEntries',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='counter',
            name='sumw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='counter',
            name='sumw2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='download',
            name='runcard_name',
            field=models.CharField(default='050720181308', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='histo1_data',
            name='numEntries',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='histo1_data',
            name='sumw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='histo1_data',
            name='sumw2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='histo1_data',
            name='sumwx',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='histo1_data',
            name='sumwx2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='histo1_data',
            name='xhigh',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='histo1_data',
            name='xlow',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_histo',
            name='numEntries',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_histo',
            name='sumw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_histo',
            name='sumw2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_histo',
            name='sumwx',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_histo',
            name='sumwx2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_profile',
            name='numEntries',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_profile',
            name='sumw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_profile',
            name='sumw2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_profile',
            name='sumwx',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_profile',
            name='sumwx2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_profile',
            name='sumwy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='overflow_underflow_profile',
            name='sumwy2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='profile1_data',
            name='numEntries',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile1_data',
            name='sumw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='profile1_data',
            name='sumw2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='profile1_data',
            name='sumwx',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='profile1_data',
            name='sumwx2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='profile1_data',
            name='sumwy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='profile1_data',
            name='sumwy2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='profile1_data',
            name='xhigh',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='profile1_data',
            name='xlow',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='runcard',
            name='runcard_name',
            field=models.CharField(default='050720181308', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='scatter1_data',
            name='xerr_n',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter1_data',
            name='xerr_p',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter1_data',
            name='xval',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter2_data',
            name='xerr_n',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter2_data',
            name='xerr_p',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter2_data',
            name='xval',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter2_data',
            name='yerr_n',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter2_data',
            name='yerr_p',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter2_data',
            name='yval',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter3_data',
            name='xerr_n',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter3_data',
            name='xerr_p',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter3_data',
            name='xval',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter3_data',
            name='yerr_n',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter3_data',
            name='yerr_p',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter3_data',
            name='yval',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter3_data',
            name='zerr_n',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter3_data',
            name='zerr_p',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scatter3_data',
            name='zval',
            field=models.FloatField(null=True),
        ),
    ]
