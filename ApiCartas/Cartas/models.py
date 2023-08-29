from django.db import models

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    id_carta = models.CharField(max_length=24,unique=True)
    nombre_carta = models.CharField(max_length=100,null=True)
    stock = models.IntegerField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)