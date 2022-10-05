from tabnanny import verbose
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30, verbose_name="Category")

    def __str__(self):
        return self.category

class Bonus(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Bonus Category")
    cashback = models.IntegerField(verbose_name="Cashback Percentage")

    def __str__(self):
        return "{}% cashback on {}".format(self.cashback, self.category)

class CreditCard(models.Model):
    name = models.CharField(max_length=30, verbose_name="Card Name")
    company = models.CharField(max_length=30, verbose_name="Card Company")
    bonuses = models.ManyToManyField(Bonus, verbose_name="Bonuses")

    def __str__(self):
        return self.name