CONTACTS APPLICATION
In this challenge, your task is to create a Contacts application using
the Django REST framework.
MODELS
The application has one model, namely Contact, with the following
fields and types:
Contact:

- id (AutoField),
- name(CharField),
- number(IntegerField)

---

---

ENDPOINTS
The following are the API endpoints:

- To add a contact, use the route 'add/contact/'
- To list all the contacts, use the route 'list/contact/'
- To filter a contact, use the route 'filter/contact/?search=<name>'
- To update a contact, use the route 'update/contact/<pk>'
- To delete a contact, use the route 'delete/contact/<pk>'

The functionalities of the endpoints are given as follows:

1. add/contact/
   This endpoint is used to add a new contact.
   Hint: Use CreateAPIView
   Input: name, number
   Response:

- {"name": ["This field may not be blank."]} - when the name field is blank
- {"number": ["A valid integer is required."]} - when the number field is blank
- {"number": ["Please enter a valid mobile number"]} - when the number does not start with 6, 7, 8, or 9 or does not contain 10 characters
- {"name": ["contact with this name already exists."]} - when the given name already exists
- {"number": ["contact with this number already exists."]} - when the given number already exists
- {"message": "Contact added successfully"} - when the contact has been added successfully with status HTTP_201_Created

2. list/contact/
   This endpoint is used to list all the contacts in the Database.
   Hint: Use ListAPIView
   Response: id, name, number in JSON format.

3. filter/contact/?search=<name>
   This endpoint is used to filter a contact based on the name.
   Hint: Use ListAPIView
   Input: name
   Response: id, name, number in JSON format.
   Sample Scenario :
   When given URL with http://0.0.0.0:8000/filter/contact/?search=Priya

4. update/contact/<pk>
   This endpoint is used to update the contact details.
   Hint: use RetrieveUpdateAPIView
   Input: id (in the URL like http://0.0.0.0:8000/1)
   Response:

- {"detail": "Not found."} when the ID is not present in the database
- {"name": ["This field may not be blank."]} when the name field is blank
- {"number": ["A valid integer is required."]} when the number field is blank
- {"number": ["Please enter a valid mobile number"]} when the number does not start with 6, 7, 8, or 9 or does not contain 10 characters
- {"message": "Contact updated successfully"} when the contact details have been updated successfully with status HTTP_200_OK

5. delete/contact/<pk>
   This endpoint is used to delete a contact.
   Hint: Use RetrieveDestroyAPIView
   Input: id (in the URL like http://0.0.0.0:8000/1)
   Response:

- {"detail": "Not found."} when the ID is not present in the database.
- On successful deletion, return a response status code HTTP 204 No Content( will be available by default. You don't have to send status)
