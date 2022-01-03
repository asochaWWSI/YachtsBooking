from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, null=True)
    surname = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)

class Yacht(models.Model):
    id = models.IntegerField(primary_key=True)
    name_yacht = models.CharField(max_length=50, null=False)
    type_yaht = models.CharField(max_length=50, null=False)
    year_of_production = models.DateField(null=False)
    engine_power = models.CharField(max_length=50, null=False)
    length = models.IntegerField(null=False)
    width = models.IntegerField(null=False)
    mass_kg = models.IntegerField(null=False)

class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    date_lend  = models.DateField(null=False)
    date_return = models.DateField(null=False)
    id_customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
    )
    id_yachts = models.ForeignKey(
        'Yacht',
        on_delete=models.CASCADE,
    )