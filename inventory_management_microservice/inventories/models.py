from django.db import models


class Inventory(models.Model):
    product_id = models.PositiveIntegerField()
    product_name = models.CharField(max_length=255, default="None")
    product_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
