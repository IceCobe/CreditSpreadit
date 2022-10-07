from rest_framework import serializers
from .models import *

class DateRangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DateRange
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')

class BonusSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Bonus
        fields = ('__all__')

class CreditCardSerializer(serializers.ModelSerializer):
    bonuses = serializers.StringRelatedField(many=True)

    class Meta:
        model = CreditCard
        fields = ('__all__')