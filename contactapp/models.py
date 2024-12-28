from django.db import models
from django.core.validators import RegexValidator

# Create 'Contact' models here 
from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=20)
    number = models.IntegerField(unique=True, validators=[RegexValidator(regex=r"^[6789]\d{9}$", message='Please enter a valid mobile number')])


