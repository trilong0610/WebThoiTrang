# Generated by Django 3.1.4 on 2020-12-21 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_auto_20201221_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 21, 22, 26, 31, 78195)),
        ),
    ]
