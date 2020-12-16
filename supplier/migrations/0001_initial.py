# Generated by Django 3.1.3 on 2020-12-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=11)),
                ('address', models.CharField(default='', max_length=255, null=True)),
            ],
        ),
    ]
