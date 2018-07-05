# Generated by Django 2.0.5 on 2018-07-05 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0012_auto_20180705_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sumw', models.FloatField()),
                ('sumw2', models.FloatField()),
                ('numEntries', models.IntegerField()),
                ('parent', models.ForeignKey(db_column='results_link', on_delete=django.db.models.deletion.DO_NOTHING, to='analyses.results_analyses')),
            ],
        ),
        migrations.AlterField(
            model_name='download',
            name='runcard_name',
            field=models.CharField(default='050720181301', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='runcard',
            name='runcard_name',
            field=models.CharField(default='050720181301', max_length=50, primary_key=True, serialize=False),
        ),
    ]
