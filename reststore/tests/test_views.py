import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from reststore.products.models import Product
from reststore.products.serializers import ProductSerializer

#initialize the APIClient
client = Client()
