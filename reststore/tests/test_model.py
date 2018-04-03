from django.test import TestCase
from reststore.products.models import Product

class ProductTest(TestCase):
    """ Test module for Product model """

    def setUp(self):
        Product.objects.create(
            idnum=0000, name='SnapBack', colour='red', brand='Gelamo',
        )
        Product.objects.create(
            idnum=9999, name='BackHat', colour='blue', brand='Gelamo'
        )

    def test_product_id(self):
        product_SnapBack = Product.objects.get(name='SnapBack')
        product_BackHat =  Product.objects.get(name='BackHat')
        self.assertEqual(
            product_SnapBack.get_brand(), "SnapBack product number 0000 is Gelamo"
        )
        self.assertEqual(
            product_BackHat.get_brand(), "BackHat product number 9999 is Gelamo"
        )