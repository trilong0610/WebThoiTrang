# Generated by Django 3.1.3 on 2020-12-20 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0010_auto_20201220_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 20, 16, 31, 37, 723656)),
        ),
    ]
