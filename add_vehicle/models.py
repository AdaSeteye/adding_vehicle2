from django.db import models

class Vehicle(models.Model):
    chassis_number = models.CharField(max_length=100)
    libre_number = models.CharField(max_length=100)
    insurance_renewal_date = models.DateField()
    edvla_renewal_date = models.DateField()


