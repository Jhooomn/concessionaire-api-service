from django.db import models


class Vehicle(models.Model):
    vid = models.CharField(max_length=999)
    type = models.CharField(max_length=999)
    brand = models.CharField(max_length=999)
    model = models.CharField(max_length=999)
    version = models.CharField(max_length=999)
    licensePlate = models.CharField(max_length=999)
    km = models.CharField(max_length=999)
    imgLink = models.CharField(max_length=999)

    class Meta:
        db_table = "vehicle"
