from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Recommendation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField()
    score = models.FloatField()
