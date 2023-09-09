from django.db import models

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    id_carta = models.CharField(max_length=24,unique=True)
    nombre_carta = models.CharField(max_length=100,null=True)
    stock = models.IntegerField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    
class Cardgames(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    games = models.IntegerField()
    sub = models.BooleanField(default=False)
    price = models.IntegerField()