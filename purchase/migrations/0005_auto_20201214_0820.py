# Generated by Django 3.1.3 on 2020-12-14 01:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_auto_20201214_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 8, 20, 41, 414388)),
        ),
    ]
