from django.shortcuts import render
from .serializers import * 
from rest_framework import viewsets      
from .models import *                 

class DateRangeView(viewsets.ModelViewSet):  
    serializer_class = DateRangeSerializer
    queryset = DateRange.objects.all()

class CategoryView(viewsets.ModelViewSet):  
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class BonusView(viewsets.ModelViewSet):  
    serializer_class = BonusSerializer
    queryset = Bonus.objects.all()

class CreditCardView(viewsets.ModelViewSet):  
    serializer_class = CreditCardSerializer
    queryset = CreditCard.objects.all()