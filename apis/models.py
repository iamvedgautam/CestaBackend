from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):

    stock_id = models.AutoField(primary_key=True)
    ticker = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.ticker


class Cesta(models.Model):

    cesta_id = models.AutoField(primary_key=True)
    cesta_name = models.CharField(unique=True, max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_json = models.JSONField()

    def __str__(self):
        return self.cesta_name


class UserPortfolio(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cesta = models.ForeignKey(Cesta, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField()
    stock_info = models.JSONField()
