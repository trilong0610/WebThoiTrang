# Generated by Django 3.1.3 on 2020-12-13 17:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20201214_0037'),
        ('purchase', '0002_auto_20201214_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AlterField(
            model_name='purchaseproduct',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 0, 37, 23, 761009)),
        ),
    ]
