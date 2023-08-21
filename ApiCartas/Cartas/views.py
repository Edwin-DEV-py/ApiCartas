from django.shortcuts import render
from .models import Card
from rest_framework.views import APIView
from rest_framework.response import Response
from concurrent.futures import ThreadPoolExecutor
from .serializers import CardSerializer
import requests

class CardView(APIView):
    def get(request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards,many=True)
        return Response(serializer.data)