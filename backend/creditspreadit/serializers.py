from rest_framework import serializers
from .models import CreditCard

class CreditSpreaditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('id','name','company')