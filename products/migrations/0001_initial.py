# Generated by Django 2.0.7 on 2018-09-01 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('sku', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('quantity', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='images/')),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]