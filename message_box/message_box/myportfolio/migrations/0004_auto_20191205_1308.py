# Generated by Django 2.2.1 on 2019-12-05 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0003_auto_20191205_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Aadhar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 5, 13, 8, 35, 151923)),
        ),
    ]
