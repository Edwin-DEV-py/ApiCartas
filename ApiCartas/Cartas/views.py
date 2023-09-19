from django.shortcuts import render
from .models import Card, Cardgames
from rest_framework.views import APIView
from rest_framework.response import Response
from concurrent.futures import ThreadPoolExecutor
from .serializers import CardSerializer, CardgamesSerializer
from rest_framework import status
from django.db.models import Q
import requests

#endpoint de todas las cartas
class example(APIView):
    def get(self,request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards,many=True)
        return Response(serializer.data)
    
    
class CardView(APIView):
    def get(self, request):
        try:
            
            #indexacion y busqueda
            tipo = request.data.get('tipo')
            heroe = request.data.get('heroe')
            
            #obtener los datos del inventario
            response = requests.get('https://cards.thenexusbattles2.cloud/api/all/')
            #response = requests.get('http://prime.bucaramanga.upb.edu.co/api/all/')
            data = response.json()

            #aplicamos paginacion para solo traer 6 cartas para la vitrina
            page_number = int(request.GET.get('page_number', 1))
            cards_per_page = 6
            total_cards = len(data)
            start_index = (page_number - 1) * cards_per_page
            end_index = start_index + cards_per_page

            page_data = data[start_index:end_index] #aqui mostramos las cartas

            card_data = []
            if tipo is None and heroe is None:
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
            
            else:
                #iterar por el json
                for carta in data:
                    #comparar el id del json con el id que pasamos
                    if carta.get('tipo', '').lower() == tipo.lower():
                        carta_data = {
                            'id_carta':carta.get('_id',''),

                        }
                        # Iterar a través de todas las propiedades del objeto
                        for key, value in carta.items():
                            if key != '_id':
                                carta_data[key] = value

                        #ahora incorporamos los datos de la DB local
                        try:
                            card_db = Card.objects.get(id_carta=carta_data['id_carta'])
                            carta_data['price'] = card_db.price
                            carta_data['stock'] = card_db.stock
                            carta_data['nombre_carta'] = card_db.nombre_carta
                        except Card.DoesNotExist:
                            pass  # No se encontró la carta
                        
                        card_data.append(carta_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)

#tipo de carta Tanque
class CardTipeTankView(APIView):
    def get(self, request):
        try:
            
            #indexacion y busqueda
            heroe = 'Guerrero Tanque'
            
            #obtener los datos del inventario
            #response = requests.get('https://cards.thenexusbattles2.cloud/api/all/')
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
            
            
            #iterar por el json
            for carta in data:
                #comparar el id del json con el id que pasamos
                if carta.get('heroe', '').lower() == heroe.lower():
                    carta_data = {
                        'id_carta':carta.get('_id',''),
                    }
                    # Iterar a través de todas las propiedades del objeto
                    for key, value in carta.items():
                        if key != '_id':
                            carta_data[key] = value
                    #ahora incorporamos los datos de la DB local
                    try:
                        card_db = Card.objects.get(id_carta=carta_data['id_carta'])
                        carta_data['price'] = card_db.price
                        carta_data['stock'] = card_db.stock
                        carta_data['nombre_carta'] = card_db.nombre_carta
                    except Card.DoesNotExist:
                        pass  # No se encontró la carta
                    
                    card_data.append(carta_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)

#tipo de carta Armas
class CardTipeGunView(APIView):
    def get(self, request):
        try:
            
            #indexacion y busqueda
            heroe = 'Guerrero Armas'
            
            #obtener los datos del inventario
            #response = requests.get('https://cards.thenexusbattles2.cloud/api/all/')
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
            
            
            #iterar por el json
            for carta in data:
                #comparar el id del json con el id que pasamos
                if carta.get('heroe', '').lower() == heroe.lower():
                    carta_data = {
                        'id_carta':carta.get('_id',''),
                    }
                    # Iterar a través de todas las propiedades del objeto
                    for key, value in carta.items():
                        if key != '_id':
                            carta_data[key] = value
                    #ahora incorporamos los datos de la DB local
                    try:
                        card_db = Card.objects.get(id_carta=carta_data['id_carta'])
                        carta_data['price'] = card_db.price
                        carta_data['stock'] = card_db.stock
                        carta_data['nombre_carta'] = card_db.nombre_carta
                    except Card.DoesNotExist:
                        pass  # No se encontró la carta
                    
                    card_data.append(carta_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)
        
#tipo de carta Fuego
class CardTipeFireView(APIView):
    def get(self, request):
        try:
            
            #indexacion y busqueda
            heroe = 'Mago Fuego'
            
            #obtener los datos del inventario
            #response = requests.get('https://cards.thenexusbattles2.cloud/api/all/')
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
            
            
            #iterar por el json
            for carta in data:
                #comparar el id del json con el id que pasamos
                if carta.get('heroe', '').lower() == heroe.lower():
                    carta_data = {
                        'id_carta':carta.get('_id',''),
                    }
                    # Iterar a través de todas las propiedades del objeto
                    for key, value in carta.items():
                        if key != '_id':
                            carta_data[key] = value
                    #ahora incorporamos los datos de la DB local
                    try:
                        card_db = Card.objects.get(id_carta=carta_data['id_carta'])
                        carta_data['price'] = card_db.price
                        carta_data['stock'] = card_db.stock
                        carta_data['nombre_carta'] = card_db.nombre_carta
                    except Card.DoesNotExist:
                        pass  # No se encontró la carta
                    
                    card_data.append(carta_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)
        
#tipo de carta Hielo
class CardTipeIceView(APIView):
    def get(self, request):
        try:
            
            #indexacion y busqueda
            heroe = 'Mago Hielo'
            
            #obtener los datos del inventario
            #response = requests.get('https://cards.thenexusbattles2.cloud/api/all/')
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
            
            
            #iterar por el json
            for carta in data:
                #comparar el id del json con el id que pasamos
                if carta.get('heroe', '').lower() == heroe.lower():
                    carta_data = {
                        'id_carta':carta.get('_id',''),
                    }
                    # Iterar a través de todas las propiedades del objeto
                    for key, value in carta.items():
                        if key != '_id':
                            carta_data[key] = value
                    #ahora incorporamos los datos de la DB local
                    try:
                        card_db = Card.objects.get(id_carta=carta_data['id_carta'])
                        carta_data['price'] = card_db.price
                        carta_data['stock'] = card_db.stock
                        carta_data['nombre_carta'] = card_db.nombre_carta
                    except Card.DoesNotExist:
                        pass  # No se encontró la carta
                    
                    card_data.append(carta_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)

#tipo de carta Veneno
class CardTipeVenenoView(APIView):
    def get(self, request):
        try:
            
            #indexacion y busqueda
            heroe = 'Pícaro Veneno'
            
            #obtener los datos del inventario
            #response = requests.get('https://cards.thenexusbattles2.cloud/api/all/')
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
            
            
            #iterar por el json
            for carta in data:
                #comparar el id del json con el id que pasamos
                if carta.get('heroe', '').lower() == heroe.lower():
                    carta_data = {
                        'id_carta':carta.get('_id',''),
                    }
                    # Iterar a través de todas las propiedades del objeto
                    for key, value in carta.items():
                        if key != '_id':
                            carta_data[key] = value
                    #ahora incorporamos los datos de la DB local
                    try:
                        card_db = Card.objects.get(id_carta=carta_data['id_carta'])
                        carta_data['price'] = card_db.price
                        carta_data['stock'] = card_db.stock
                        carta_data['nombre_carta'] = card_db.nombre_carta
                    except Card.DoesNotExist:
                        pass  # No se encontró la carta
                    
                    card_data.append(carta_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)
        
#tipo de carta Machete
class CardTipeMacheteView(APIView):
    def get(self, request):
        try:
            
            #indexacion y busqueda
            heroe = 'Pícaro Machete'
            
            #obtener los datos del inventario
            #response = requests.get('https://cards.thenexusbattles2.cloud/api/all/')
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
            
            
            #iterar por el json
            for carta in data:
                #comparar el id del json con el id que pasamos
                if carta.get('heroe', '').lower() == heroe.lower():
                    carta_data = {
                        'id_carta':carta.get('_id',''),
                    }
                    # Iterar a través de todas las propiedades del objeto
                    for key, value in carta.items():
                        if key != '_id':
                            carta_data[key] = value
                    #ahora incorporamos los datos de la DB local
                    try:
                        card_db = Card.objects.get(id_carta=carta_data['id_carta'])
                        carta_data['price'] = card_db.price
                        carta_data['stock'] = card_db.stock
                        carta_data['nombre_carta'] = card_db.nombre_carta
                    except Card.DoesNotExist:
                        pass  # No se encontró la carta
                    
                    card_data.append(carta_data)

            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)

#ver el detalle de cada carta
class CardDetail(APIView):
    def get(self, request, id_carta):
        try:
            
            #obtener los datos del inventario
            response = requests.get('https://cards.thenexusbattles2.cloud/api/all/')
            #response = requests.get('http://prime.bucaramanga.upb.edu.co/api/all/')
            data = response.json()

            card_data = []
            
            #iterar por el json
            for carta in data:
                #comparar el id del json con el id que pasamos
                if carta.get('_id') == id_carta:
                    card_data = carta
                    pass
            
            #ahora incorporamos los datos de la DB local
            try:
                card_db = Card.objects.get(id_carta=id_carta)
                card_data['price'] = card_db.price
                card_data['stock'] = card_db.stock
                card_data['nombre_carta'] = card_db.nombre_carta
            except Card.DoesNotExist:
                pass  # No se encontró la carta
            
            return Response(card_data)

        except Exception as e:
            return Response({'error': 'Error al obtener datos'}, status=500)
        
            

#endpoint de personajes
class CardCharacterView(APIView):
    def get(self, request):
        try:
            
            #obtener los datos del inventario
            response = requests.get('https://cards.thenexusbattles2.cloud/api/heroes/?page_size=6&page_number=1')
            data = response.json()

            card_data = []

            #aca mapeamos los datos para unirlos con la inforacion de la DB de precios y stock
            for carta_data in data:
                id_carta = carta_data.get('Id', '')

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
        
#endpoint de armas
class CardGunView(APIView):
    def get(self, request):
        try:
            
            #obtener los datos del inventario
            response = requests.get('https://cards.thenexusbattles2.cloud/api/armas/?page_size=12&page_number=1')
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
        
#endpoint de armaduras
class CardArmorView(APIView):
    def get(self, request):
        try:
            
            #obtener los datos del inventario
            response = requests.get('https://cards.thenexusbattles2.cloud/api/armaduras/?page_size=6&page_number=1')
            data = response.json()

            card_data = []

            #aca mapeamos los datos para unirlos con la inforacion de la DB de precios y stock
            for carta_data in data:
                id_carta = carta_data.get('Id', '')

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

#endpoint de items
class CardItemsView(APIView):
    def get(self, request):
        try:
            
            #obtener los datos del inventario
            response = requests.get('https://cards.thenexusbattles2.cloud/api/items/?page_size=6&page_number=1')
            data = response.json()

            card_data = []

            #aca mapeamos los datos para unirlos con la inforacion de la DB de precios y stock
            for carta_data in data:
                id_carta = carta_data.get('Id', '')

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
        
#endpoint de membresias
class Membership(APIView):
    def get(self,request):
        cards = Cardgames.objects.all()
        serializer = CardgamesSerializer(cards,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



#endpoint de prueba
class Cards(APIView):
    def get(self,request):
        card = Card.objects.all()
        serializer = CardSerializer(card,many=True)
        return Response(serializer.data)
                
