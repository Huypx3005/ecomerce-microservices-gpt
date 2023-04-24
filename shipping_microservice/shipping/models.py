# models.py

from django.db import models
from django.contrib.auth.models import User


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=255)


class Shipment(models.Model):
    order_id = models.IntegerField()
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    carrier = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=255)
    estimated_delivery_date = models.DateField()
    actual_delivery_date = models.DateField(null=True, blank=True)
