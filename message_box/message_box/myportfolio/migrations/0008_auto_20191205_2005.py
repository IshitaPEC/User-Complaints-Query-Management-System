# Generated by Django 2.2.1 on 2019-12-05 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0007_auto_20191205_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='complaint_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 5, 20, 5, 40, 126948)),
        ),
    ]
