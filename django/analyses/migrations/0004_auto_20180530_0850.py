# Generated by Django 2.0.5 on 2018-05-30 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0003_auto_20180521_1639'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='used_analyses',
            unique_together={('modelname', 'anaid')},
        ),
    ]
