from django.contrib import admin
from .models import Card, Cardgames

class CardAdmin(admin.ModelAdmin):
    list_display = ('id_carta','nombre_carta' ,'stock', 'price')
    
class CardgamesAdmin(admin.ModelAdmin):
    list_display = ('id_carta','title' ,'games','sub', 'price')

admin.site.register(Card,CardAdmin)
admin.site.register(Cardgames,CardgamesAdmin)