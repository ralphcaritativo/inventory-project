# Generated by Django 2.0.7 on 2018-09-01 16:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_auto_20180901_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 16, 2, 48, 4865, tzinfo=utc)),
        ),
    ]
