# Generated by Django 2.0.5 on 2018-07-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0007_auto_20180704_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='runcard_name',
            field=models.CharField(default='040720181446', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='results_analyses',
            name='xyd',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='runcard',
            name='runcard_name',
            field=models.CharField(default='040720181446', max_length=50, primary_key=True, serialize=False),
        ),
    ]
