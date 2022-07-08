from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default=None, blank=True, null=True)
    phone = models.IntegerField(default=None, blank=True, null=True)
    birthday = models.DateTimeField(default=None, blank=True, null=True)

class Product(models.Model):
    reference = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    stock = models.IntegerField()
    purchase_price = models.FloatField()
    sale_price = models.FloatField()

class Bill(models.Model):
    seller = models.ForeignKey("User", on_delete=models.CASCADE)
    customer = models.ForeignKey("Person", on_delete=models.CASCADE)
    total = models.FloatField()
    date = models.DateTimeField()

class SaleDetail(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    bill = models.ForeignKey("Bill", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    total = models.FloatField()