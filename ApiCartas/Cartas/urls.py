from django.urls import path
from .views import *

urlpatterns = [
    path('cards/',CardView.as_view(),name='Cartas')
]
