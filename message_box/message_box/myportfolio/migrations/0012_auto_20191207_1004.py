# Generated by Django 2.2.1 on 2019-12-07 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0011_auto_20191205_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 10, 4, 34, 120326)),
        ),
    ]
