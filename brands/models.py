from django.db import models
from django.utils import timezone


# Create your models here.
STATUS_CHOICES = [
        (0, 'Inactive'),
        (1, 'Active'),
    ]

class Brand(models.Model):
    name = models.CharField(max_length = 255)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 0)
    pub_date = models.DateTimeField(default = timezone.now)




    def __str__(self):
        return self.name
        return self.status
