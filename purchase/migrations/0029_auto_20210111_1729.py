# Generated by Django 3.1.4 on 2021-01-11 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0028_auto_20210111_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 17, 29, 25, 21723)),
        ),
    ]
