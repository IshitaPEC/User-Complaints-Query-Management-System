# Generated by Django 2.2.1 on 2019-12-07 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0018_auto_20191207_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_reconsider',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='reconsider_aig',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='reconsider_dgp',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 22, 22, 2, 215745), null=True),
        ),
    ]
