from django.db import models

# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    square = models.CharField(max_length=64)
    price = models.IntegerField()
    ownerName = models.CharField(max_length=128)
    ownerContact = models.CharField(max_length=256)
    sold = models.BooleanField(default=False)


    def __str__(self):
        return self.name