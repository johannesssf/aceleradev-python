from django.test import TestCase

from .models import Product


class ProductStrTestCase(TestCase):

    def test_prod_str_equal_prod_name(self):
        product = Product.objects.create(
            name='Test Name',
            description='Test Description',
            price=10.5,
        )
        self.assertEqual(product.name, 'Test Name')
