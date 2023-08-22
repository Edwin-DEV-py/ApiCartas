from django.urls import path
from .views import *

urlpatterns = [
    path('cards/',Cards.as_view(),name='Cartas')
]
