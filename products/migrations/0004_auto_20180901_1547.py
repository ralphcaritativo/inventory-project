# Generated by Django 2.0.7 on 2018-09-01 15:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 15, 47, 47, 975890, tzinfo=utc)),
        ),
    ]
