from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.utils import json


class ContactTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_add_contact(self):
        payload = {'name': 'test', 'number': '6123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"message": "Contact added successfully"})

        # try to add contact without name
        payload = {'name': '', 'number': '7123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"name": ["This field may not be blank."]})

        # try to add contact without number
        payload = {'name': 'demo', 'number': ''}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"number": ["A valid integer is required."]})

        # try to add contact with invalid number
        payload = {'name': 'demo', 'number': '123213'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"number": ["Please enter a valid mobile number"]})

        # try to add contact with already existing name
        payload = {'name': 'test', 'number': '7123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"name": ["contact with this name already exists."]})

        # try to add contact with already existing number
        payload = {'name': 'demo', 'number': '6123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"number": ["contact with this number already exists."]})

        # add contact
        payload = {'name': 'demo', 'number': '7123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"message": "Contact added successfully"})

        
    def test_list_contact(self):
        payload = {'name': 'test', 'number': '6123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"message": "Contact added successfully"})

        payload = {'name': 'demo', 'number': '7123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"message": "Contact added successfully"})
       
        # list contact
        response = self.client.get('/list/contact/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, [{"id": 1, "name": "test", "number": 6123456780},
                                                {"id": 2, "name": "demo", "number": 7123456780}])


    def test_filter_contact(self):
        payload = {'name': 'test', 'number': '6123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"message": "Contact added successfully"})

        payload = {'name': 'demo', 'number': '7123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"message": "Contact added successfully"})
        
        # filter contact
        response = self.client.get('/filter/contact/?search=test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, [{"id": 1, "name": "test", "number": 6123456780}])

        response = self.client.get('/filter/contact/?search=de')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, [{"id": 2, "name": "demo", "number": 7123456780}])


    def test_update_contact(self):
        payload = {'name': 'test', 'number': '6123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"message": "Contact added successfully"})

        payload = {'name': 'demo', 'number': '7123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"message": "Contact added successfully"})
        
        payload = {'number': '8123456780'}
        response = self.client.patch('/update/contact/5', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"detail":"Not found."})

        # try to update contact without name      
        payload = {'name': ''}
        response = self.client.patch('/update/contact/2', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"name": ["This field may not be blank."]})

        # try to update contact without number
        payload = {'number': ''}
        response = self.client.patch('/update/contact/2', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"number": ["A valid integer is required."]})

        # try to update contact with invalid number      
        payload = {'number': '01010101'}
        response = self.client.patch('/update/contact/2', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"number": ["Please enter a valid mobile number"]})

        # update contact
        payload = {'number': '8123456780'}
        response = self.client.patch('/update/contact/2', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"message":"Contact updated successfully"})


    def test_delete_contact(self):
        payload = {'name': 'test', 'number': '6123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"message": "Contact added successfully"})

        payload = {'name': 'demo', 'number': '7123456780'}
        response = self.client.post('/add/contact/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"message": "Contact added successfully"})
        
        response = self.client.delete('/delete/contact/5')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"detail": "Not found."})

        # delete 
        response = self.client.delete('/delete/contact/2')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)    

        response = self.client.delete('/delete/contact/2')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"detail": "Not found."})


