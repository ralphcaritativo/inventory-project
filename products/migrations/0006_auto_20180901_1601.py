# Generated by Django 2.0.7 on 2018-09-01 16:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180901_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 16, 1, 8, 383002, tzinfo=utc)),
        ),
    ]
