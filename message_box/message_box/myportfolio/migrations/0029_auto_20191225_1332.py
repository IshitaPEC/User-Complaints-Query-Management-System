# Generated by Django 2.2.1 on 2019-12-25 08:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0028_auto_20191225_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='log_in',
        ),
        migrations.AlterField(
            model_name='message',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 13, 32, 17, 432105), null=True),
        ),
    ]
