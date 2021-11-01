from django.db import models


class Vehicle(models.Model):
    vid = models.CharField(max_length=20)
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=15)
    version = models.CharField(max_length=15)
    licensePlate = models.CharField(max_length=15)
    km = models.CharField(max_length=15)
    imgLink = models.CharField(max_length=999)

    class Meta:
        db_table = "vehicle"
