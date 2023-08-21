from django.shortcuts import render
from .models import Card
from rest_framework.views import APIView
from rest_framework.response import Response
from concurrent.futures import ThreadPoolExecutor
from .serializers import CardSerializer
import requests

class CardView(APIView):
    def get(self,request):
        try:
            all_cards = Card.objects.all()
            card_data = []
            
            def get_card_data(card_item):
                id_carta = card_item.id_carta
                price = card_item.price
                stock = card_item.stock
                
                response = requests.get('') #endpoint del inventario
                data = response.json()
                
                card_item_data = {
                    'id_carta': id_carta,
                    'name': data['name'],
                    'description':data['description'],
                    'price':price,
                    'stock': stock
                }
                
                return card_item_data
            
            with ThreadPoolExecutor() as executor:
                card_data = list(executor.map(get_card_data, all_cards))
                
            return Response(card_data)
        
        except Card.DoesNotExist:
            return Response({'error':'No hay cartas'}, status=404)
                