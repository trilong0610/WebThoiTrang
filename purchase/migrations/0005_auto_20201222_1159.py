# Generated by Django 3.1.4 on 2020-12-22 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_auto_20201221_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 22, 11, 59, 18, 154422)),
        ),
    ]
