# Generated by Django 2.0.7 on 2018-09-01 16:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_auto_20180901_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='brand',
            name='status',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0),
        ),
    ]