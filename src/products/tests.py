from django.test import TestCase
from .models import Product

# Create your tests here.

class ProductTests(TestCase):
   """
   Here are defined the tests that run againts our Product model
   """

   def test_str(self):
      test_title = Product(title='A product')
      self.assertEqual(str(test_title), 'A product')