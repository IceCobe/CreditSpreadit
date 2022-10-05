from django.shortcuts import render
from .serializers import CreditSpreaditSerializer 
from rest_framework import viewsets      
from .models import CreditCard                 

class CreditSpreaditView(viewsets.ModelViewSet):  
    serializer_class = CreditSpreaditSerializer
    queryset = CreditCard.objects.all()