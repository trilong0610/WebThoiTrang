# Generated by Django 3.1.4 on 2021-01-10 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210110_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sizeproduct',
            name='amount_sell',
        ),
    ]
