from tabnanny import verbose
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# Run this to nuke everything
# python manage.py migrate --run-syncdb

class DateRange(models.Model):
    name = models.CharField(max_length=30, verbose_name="Quarter")

    active_start = models.DateField(verbose_name="Activate Date Start")
    active_end = models.DateField(verbose_name="Activate Date End")

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=30, verbose_name="Category")

    def __str__(self):
        return self.category

class Bonus(models.Model):
    category = models.ManyToManyField(Category, verbose_name="Bonus Category")
    dates = models.ForeignKey(DateRange, on_delete=models.CASCADE, verbose_name="Active Date Range")
    cashback = models.IntegerField(verbose_name="Cashback Percentage")

    def __str__(self):
        if self.category.count() == 1:
            return "{}% cashback on {} during {}".format(self.cashback, self.category.all()[0], self.dates)
        else:
            return "{}% cashback on top category between during {}".format(self.cashback, self.dates)
class CreditCard(models.Model):
    name = models.CharField(max_length=100, verbose_name="Card Name")
    company = models.CharField(max_length=30, verbose_name="Card Company")
    bonuses = models.ManyToManyField(Bonus, verbose_name="Bonuses")

    def __str__(self):
        return self.name