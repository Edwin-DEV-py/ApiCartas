from django.shortcuts import render
from .models import Card
from rest_framework.views import APIView
from rest_framework.response import Response
from concurrent.futures import ThreadPoolExecutor
from .serializers import CardSerializer
import requests

class CardView(APIView):
    def get(self, request):
        try:
            response = requests.get('http://prime.bucaramanga.upb.edu.co/api/heroes/?page_size=6&page_number=1')
            data = response.json()

            card_data = []

            for carta_data in data:
                id_carta = carta_data.get('Id', '')
                hero_name = carta_data.get('Clase', '')
                desc = carta_data.get('Tipo', '')

                try:
                    card_db = Card.objects.get(id_carta=id_carta)
                    price = card_db.price
                    stock = card_db.stock

                    card_item_data = {
                        'id_carta': id_carta,
                        'name': hero_name,
                        'description': desc,
                        'price': price,
                        'stock': stock
                    }

                    card_data.append(card_item_data)
                except Card.DoesNotExist:
                    pass  # No se encontró la carta en la base de datos

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)

        
class Cards(APIView):
    def get(self,request):
        card = Card.objects.all()
        serializer = CardSerializer(card,many=True)
        return Response(serializer.data)
                