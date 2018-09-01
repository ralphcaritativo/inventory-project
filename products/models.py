from django.db import models

# Create your models here.

# class Status(models.Model):
#     name = models.CharField(max_length = 255)
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    sku = models.CharField(max_length = 255)
    price = models.DecimalField(default = 0.00, max_digits = 9, decimal_places = 2)
    quantity = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = 'images/')
    pub_date = models.DateTimeField()

    # status = models.CharField(max_length = 255, default = 'Inactive')


    def __str__(self):
        return self.name

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
