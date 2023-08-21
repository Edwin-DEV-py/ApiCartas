from django.db import models

class Card(models.Model):
    id_carta = models.IntegerField()
    stock = models.IntegerField()
    price = models.DecimalField(max_digits = 6,decimal_places = 2)