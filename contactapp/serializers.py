from rest_framework import serializers
from .models import Contact

# Serializer Name 'ContactSerializer'
class ContactSerializer(serializers.ModelSerializer):
    """Class Serializing the Contact Models"""
    class Meta:
        """The Meta class"""
        model = Contact
        fields = ['id', 'name', 'number']
    
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("This field may not be blank")
        if Contact.objects.filter(name=value).exists():
            raise serializers.ValidationError("contact with this name already exists")
        return value
    
    def validate_number(self, value):
        if not value:
            raise serializers.ValidationError("A valid integer is required")
        if not str(value).isdigit():
            raise serializers.ValidationError("A valid integer is required")
        if not (str(value).startswith(('6', '7', '8', '9')) and len(str(value)) == 10):
            raise serializers.ValidationError("Please enter a valid mobile number")
        if Contact.objects.filter(number=value).exists():
            raise serializers.ValidationError("contact with this number already exists.")
        return value
