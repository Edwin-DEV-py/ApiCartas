from django.shortcuts import render
from .models import Card
from rest_framework.views import APIView
from rest_framework.response import Response
from concurrent.futures import ThreadPoolExecutor
from .serializers import CardSerializer
import requests

#endpoint de todas las cartas
class CardView(APIView):
    def get(self, request):
        try:
            
            #obtener los datos del inventario
            #response = requests.get('https://main-api-cartas.thenexusbattles2.com/api/all/')
            response = requests.get('http://prime.bucaramanga.upb.edu.co/api/all/')
            data = response.json()

            #aplicamos paginacion para solo traer 6 cartas para la vitrina
            page_number = int(request.GET.get('page_number', 1))
            cards_per_page = 6
            total_cards = len(data)
            start_index = (page_number - 1) * cards_per_page
            end_index = start_index + cards_per_page

            page_data = data[start_index:end_index] #aqui mostramos las cartas

            card_data = []

            #aca mapeamos los datos para unirlos con la inforacion de la DB de precios y stock
            for carta_data in page_data:
                id_carta = carta_data.get('_id', '')

                card_item_data = {
                    'id_carta': id_carta,
                }

                # Iterar a través de todas las propiedades del objeto
                for key, value in carta_data.items():
                    if key != '_id':
                        card_item_data[key] = value

                try:
                    card_db = Card.objects.get(id_carta=id_carta)
                    card_item_data['price'] = card_db.price
                    card_item_data['stock'] = card_db.stock
                    card_item_data['nombre_carta'] = card_db.nombre_carta
                except Card.DoesNotExist:
                    pass  # No se encontró la carta

                card_data.append(card_item_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)

#ver el detalle de cada carta
class CardDetail(APIView):
    def get(self, request, id_carta):
        try:
            response = requests.get(f'https://main-api-cartas.thenexusbattles2.com/api/all/{id_carta}')
            data = response.json()
            
            card_db = Card.objects.get(id_carta=id_carta)
            
            card_data = {
                'id_carta':id_carta,
                'price':card_db.price,
                'stock':card_db.stock,
                'nombre_carta': card_db.nombre_carta,
                **data #desempaquetar rapidamente todos los elementos del diccionario
            }
            
            return Response(card_data)
        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)
        
            

#endpoint de personajes
class CardCharacterView(APIView):
    def get(self, request):
        try:
            
            #obtener los datos del inventario
            response = requests.get('http://prime.bucaramanga.upb.edu.co/api/heroes/?page_size=6&page_number=1')
            data = response.json()

            card_data = []

            #aca mapeamos los datos para unirlos con la inforacion de la DB de precios y stock
            for carta_data in data:
                id_carta = carta_data.get('Id', '')

                card_item_data = {
                    'Id': id_carta,
                }

                # Iterar a través de todas las propiedades del objeto
                for key, value in carta_data.items():
                    if key != '_id':
                        card_item_data[key] = value

                try:
                    card_db = Card.objects.get(id_carta=id_carta)
                    card_item_data['price'] = card_db.price
                    card_item_data['stock'] = card_db.stock
                    card_item_data['nombre_carta'] = card_db.nombre_carta
                except Card.DoesNotExist:
                    pass  # No se encontró la carta

                card_data.append(card_item_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)
        
#endpoint de armas
class CardGunView(APIView):
    def get(self, request):
        try:
            
            #obtener los datos del inventario
            response = requests.get('http://prime.bucaramanga.upb.edu.co/api/armas/?page_size=12&page_number=1')
            data = response.json()

            #aplicamos paginacion para solo traer 6 cartas para la vitrina
            page_number = int(request.GET.get('page_number', 1))
            cards_per_page = 6
            total_cards = len(data)
            start_index = (page_number - 1) * cards_per_page
            end_index = start_index + cards_per_page

            page_data = data[start_index:end_index] #aqui mostramos las cartas

            card_data = []

            #aca mapeamos los datos para unirlos con la inforacion de la DB de precios y stock
            for carta_data in page_data:
                id_carta = carta_data.get('Id', '')

                card_item_data = {
                    'Id': id_carta,
                }

                # Iterar a través de todas las propiedades del objeto
                for key, value in carta_data.items():
                    if key != '_id':
                        card_item_data[key] = value

                try:
                    card_db = Card.objects.get(id_carta=id_carta)
                    card_item_data['price'] = card_db.price
                    card_item_data['stock'] = card_db.stock
                    card_item_data['nombre_carta'] = card_db.nombre_carta
                except Card.DoesNotExist:
                    pass  # No se encontró la carta

                card_data.append(card_item_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)
        
#endpoint de armaduras
class CardArmorView(APIView):
    def get(self, request):
        try:
            
            #obtener los datos del inventario
            response = requests.get('http://prime.bucaramanga.upb.edu.co/api/armaduras/?page_size=6&page_number=1')
            data = response.json()

            card_data = []

            #aca mapeamos los datos para unirlos con la inforacion de la DB de precios y stock
            for carta_data in data:
                id_carta = carta_data.get('Id', '')

                card_item_data = {
                    'Id': id_carta,
                }

                # Iterar a través de todas las propiedades del objeto
                for key, value in carta_data.items():
                    if key != '_id':
                        card_item_data[key] = value

                try:
                    card_db = Card.objects.get(id_carta=id_carta)
                    card_item_data['price'] = card_db.price
                    card_item_data['stock'] = card_db.stock
                    card_item_data['nombre_carta'] = card_db.nombre_carta
                except Card.DoesNotExist:
                    pass  # No se encontró la carta

                card_data.append(card_item_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)

#endpoint de items
class CardItemsView(APIView):
    def get(self, request):
        try:
            
            #obtener los datos del inventario
            response = requests.get('http://prime.bucaramanga.upb.edu.co/api/items/?page_size=6&page_number=1')
            data = response.json()

            card_data = []

            #aca mapeamos los datos para unirlos con la inforacion de la DB de precios y stock
            for carta_data in data:
                id_carta = carta_data.get('Id', '')

                card_item_data = {
                    'Id': id_carta,
                }

                # Iterar a través de todas las propiedades del objeto
                for key, value in carta_data.items():
                    if key != '_id':
                        card_item_data[key] = value

                try:
                    card_db = Card.objects.get(id_carta=id_carta)
                    card_item_data['price'] = card_db.price
                    card_item_data['stock'] = card_db.stock
                    card_item_data['nombre_carta'] = card_db.nombre_carta
                except Card.DoesNotExist:
                    pass  # No se encontró la carta

                card_data.append(card_item_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)




#endpoint de prueba
class Cards(APIView):
    def get(self,request):
        card = Card.objects.all()
        serializer = CardSerializer(card,many=True)
        return Response(serializer.data)
                
