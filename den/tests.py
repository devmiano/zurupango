from django.test import TestCase
from .models import Cat, Category, Location

class LocationTestCase(TestCase):
  def setUp(self):
    self.mali = Location(url='mali', title='Mali')
    
  def test_instance(self):
    self.assertTrue(isinstance(self.mali, Location))
    
  def test_save_location(self):
    self.mali.save_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations) > 0)
    
class CategoryTestCase(TestCase):
  def setUp(self):
    self.tiger = Category(image='category/tiger.png', url='tigers', title='Tiger', genus='Panthera tigris', caption='New Tiger')
    
  def test_instance(self):
    self.assertTrue(isinstance(self.tiger, Category))

# class CatTestCase(TestCase):
#   def setUp(self):
#     self
