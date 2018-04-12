from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    """
    Defined a ModelSerializer that validates the fields
    and provides one to one relationship with the API
    endpoints(urls) and models
    """
    class Meta:
        model = Product
        fields = ('idnum', 'name', 'colour', 'brand', 'created_at', 'updated_at')
