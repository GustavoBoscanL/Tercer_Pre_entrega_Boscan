from django.db import models

class User(models.Model):
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField()
    car_brand = models.CharField(max_length=60)
    car_plate = models.CharField(max_length=60)

class Employees(models.Model):
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField()
    age = models.IntegerField()
    position = models.CharField(max_length=60)
    
class Washing_prices(models.Model):
    car_type = models.CharField(max_length=60)
    price = models.FloatField()
    

