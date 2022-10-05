from rest_framework import serializers
from .models import Bonus, CreditCard

class CreditSpreaditSerializer(serializers.ModelSerializer):

    bonuses = serializers.StringRelatedField(many=True)

    class Meta:
        model = CreditCard
        fields = ('id','name','company', 'bonuses')