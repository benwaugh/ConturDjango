# Generated by Django 2.0.5 on 2018-08-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0005_auto_20180809_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bsm_model',
            name='UFO_Link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='download',
            name='runcard_name',
            field=models.CharField(default='130820181135', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='runcard',
            name='runcard_name',
            field=models.CharField(default='130820181135', max_length=50, primary_key=True, serialize=False),
        ),
    ]
