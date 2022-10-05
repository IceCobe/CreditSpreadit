from django.db import models

# Create your models here.
class CreditCard(models.Model):
    name = models.CharField(max_length=30, verbose_name="Card Name")
    company = models.CharField(max_length=30, verbose_name="Card Company")