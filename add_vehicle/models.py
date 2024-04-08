from django.db import models

class Vehicle(models.Model):
    chassis_number = models.CharField(max_length=100)
    libre_number = models.CharField(max_length=100)
    document_renewal_date = models.DateField()
    insurance_renewal_date = models.DateField()
