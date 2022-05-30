from django.test import TestCase
from .models import Cat, Category, Location

class LocationTestCase(TestCase):
  def setUp(self):
    self.mali = Location(url='mali', title='Mali')
    
  def test_instance(self):
    self.assertTrue(isinstance(self.mali, Location))
    
# class CategoryTestCase(TestCase):
#   def setUp(self):
#     self

# class CatTestCase(TestCase):
#   def setUp(self):
#     self
