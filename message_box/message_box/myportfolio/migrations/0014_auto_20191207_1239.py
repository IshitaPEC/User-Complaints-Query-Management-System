# Generated by Django 2.2.1 on 2019-12-07 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0013_auto_20191207_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_actiontaken',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 12, 39, 9, 42158)),
        ),
    ]
