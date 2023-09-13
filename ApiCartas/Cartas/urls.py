from django.urls import path
from .views import *

urlpatterns = [
    path('cards/',CardView.as_view(),name='Cartas'),
    path('membership/',CardgamesView.as_view(),name='Membresias'),
    path('cards2/',example.as_view(),name='Cartas2'),#prueba
    path('cardDetail/<str:id_carta>',CardDetail.as_view(),name='Detalle'),
    path('characters/',CardCharacterView.as_view(),name='Personajes'),
    path('guns/',CardGunView.as_view(),name='Personajes'),
    path('armors/',CardArmorView.as_view(),name='Personajes'),
    path('items/',CardItemsView.as_view(),name='Personajes'),
]
