from django.urls import path
from .views import *

urlpatterns = [
    path('cards/',CardView.as_view(),name='Cartas'),
    path('membership/',Membership.as_view(),name='Membresias'),
    path('cards2/',example.as_view(),name='Cartas2'),#prueba
    path('cardDetail/<str:id_carta>',CardDetail.as_view(),name='Detalle'),
    path('characters/',CardCharacterView.as_view(),name='Personajes'),
    path('guns/',CardGunView.as_view(),name='Personajes'),
    path('armors/',CardArmorView.as_view(),name='Personajes'),
    path('items/',CardItemsView.as_view(),name='Personajes'),
    #tipos
    path('Tanque/',CardTipeTankView.as_view(),name='Tanque'),
    path('Armas/',CardTipeGunView.as_view(),name='Armas'),
    path('Fuego/',CardTipeFireView.as_view(),name='Fuego'),
    path('Hielo/',CardTipeIceView.as_view(),name='Hielo'),
    path('Veneno/',CardTipeVenenoView.as_view(),name='Vneneo'),
    path('Machete/',CardTipeMacheteView.as_view(),name='Machete'),
]
