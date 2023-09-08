from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch

#crear clase para probar que se pueden traer las cartas del inventario y se puedan mostrar
class CardViewTest(TestCase):
    
    #la primera prueba para verificar que si puede extraer los datos
    @patch('requests.get')  # Simulamos la solicitud a la API externa
    def test_getAllCards_success(self, mock):
        data = [{'_id':1, 'name': 'Carta 1'},{'_id':2, 'name': 'Carta 2'}]
        mock.return_value.json.return_value = data
        
        url = reverse('Cartas')
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(data))
        
        print('Prueba para obtener todas las cartas')
        print('Prueba Exitosa: Se obtuvieron todas las cartas, en total son:',len(data))
    
    #la segunda prueba lanza un error porque no puede extraer los datos
    @patch('requests.get')  # Simulamos la solicitud a la API externa
    def test_getAllCards_failure(self, mock):
        mock.side_effect = Exception("Error al obtener datos (Simulado)")
        
        
        url = reverse('Cartas')
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn('error', response.data)
        
        print('Prueba para obtener verificar la respuesta negativa')
        print('Prueba Exitosa: El servidor no logro extraer los datos, por lo tanto devuelve un mensaje')
        print('----------------------------------------------------------------------------------------')