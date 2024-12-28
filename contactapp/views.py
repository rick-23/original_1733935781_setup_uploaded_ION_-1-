from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .models import Contact
from .serializers import ContactSerializer

# Method to add contact
# className ---> AddContactView 
class AddContactView(generics.CreateAPIView):
    """Add Contact View """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == 201:
            return Response(
              {"message": "Contact added successfully"},
              status=status.HTTP_201_CREATED
            )
        return response

# Method to list all contacts
# className ---> ListContactView 
class ListContactView(generics.ListAPIView):
    """List Contacts View"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# Method to filter contact
# className ---> FilterContactView
class FilterContactView(generics.ListAPIView):
    """Filter Contacts View"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

# Method to update contact
# className ---> UpdateContactView
class UpdateContactView(generics.RetrieveUpdateAPIView):
    """Update Contact View"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    def update(self, request, *args, **kwargs):
        try:
            contact = self.get_object()
        except Contact.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            return Response({"message":"Contact updated successfully"}, status=200)
        return response

# Method to delete contact 
# className ---> DeleteContactView  
class DeleteContactView(generics.RetrieveDestroyAPIView):
    """Delete Contact View"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    def delete(self, request, *args, **kwargs):
        try:
            contact = self.get_object()
        except Contact.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)
        return super().delete(request, *args, **kwargs)







