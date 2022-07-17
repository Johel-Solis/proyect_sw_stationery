from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_type = models.CharField(max_length=10, default="seller")
    

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, default=None, blank=True, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default=None, blank=True, null=True)
    phone = models.IntegerField(default=None, blank=True, null=True)
    birthday = models.DateTimeField(default=None, blank=True, null=True)

class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField(default=None, blank=True, null=True)
    email = models.CharField(max_length=50, default=None, blank=True, null=True)
    
    
class Product(models.Model):
    reference = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    stock = models.IntegerField()
    brand = models.CharField(max_length=50)
    purchase_price = models.FloatField()
    sale_price = models.FloatField()
    description = models.CharField(max_length=60, default=None, blank=True, null=True)

class Bill(models.Model):
    seller = models.ForeignKey("User", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    total = models.FloatField()
    date = models.DateTimeField()

class SaleDetail(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    bill = models.ForeignKey("Bill", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    total = models.FloatField()