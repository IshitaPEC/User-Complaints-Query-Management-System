# Generated by Django 2.2.1 on 2019-12-05 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0010_auto_20191205_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='action_taken',
            field=models.CharField(default='No action yet', max_length=1000),
        ),
        migrations.AlterField(
            model_name='message',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 5, 20, 34, 51, 333136)),
        ),
    ]
