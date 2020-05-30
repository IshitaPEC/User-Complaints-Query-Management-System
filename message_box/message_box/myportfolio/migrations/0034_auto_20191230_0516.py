# Generated by Django 2.0.7 on 2019-12-30 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0033_auto_20191226_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Aadhar',
            field=models.PositiveIntegerField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='PIN_Code',
            field=models.PositiveIntegerField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 5, 16, 48, 967075), null=True),
        ),
    ]
