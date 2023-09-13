from rest_framework import serializers
from .models import Card, Cardgames

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
        
class CardgamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardgames
        fields = '__all__'