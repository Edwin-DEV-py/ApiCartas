from django.db import models

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    id_carta = models.CharField(max_length=24,unique=True)
    nombre_carta = models.CharField(max_length=100,null=True)
    stock = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    is_available = models.BooleanField(default=True)
    discount = models.BooleanField(default=False)
    
class Cardgames(models.Model):
    id_carta = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    games = models.IntegerField()
    sub = models.BooleanField(default=False)
    img = models.CharField(max_length=300)
    price = models.IntegerField()