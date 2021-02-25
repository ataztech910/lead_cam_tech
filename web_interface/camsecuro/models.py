from django.db import models


# Create your models here.
class Cities(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name


class Addresses(models.Model):
    address = models.CharField(max_length=2000)
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE)
    coordinates = models.CharField(max_length=100)
    def __str__(self):
        return self.address


class Cameras(models.Model):
    description = models.CharField(max_length=500)
    uuid = models.CharField(max_length=200)
    address_id = models.ForeignKey(Addresses, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
