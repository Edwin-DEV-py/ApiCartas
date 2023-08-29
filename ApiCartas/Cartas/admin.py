from django.contrib import admin
from .models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('id_carta','nombre_carta' ,'stock', 'price')

admin.site.register(Card,CardAdmin)
