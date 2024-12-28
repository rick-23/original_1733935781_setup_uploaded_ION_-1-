"""contacts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from contactapp.views import AddContactView, ListContactView, FilterContactView, UpdateContactView, DeleteContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/contact/', AddContactView.as_view(), name='add_contact'),
    path('list/contact/', ListContactView.as_view(), name='list_contact'),
    path('filter/contact/', FilterContactView.as_view(), name='filter_contact'),
    path('update/contact/<pk>', UpdateContactView.as_view(), name='update_contact'),
    path('delete/contact/<pk>', DeleteContactView.as_view(), name='delete_contact')
]

