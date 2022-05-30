from django.db import models
from django.utils import timezone
import datetime


class Location(models.Model):
  url = models.CharField(max_length=48)
  title = models.CharField(max_length=200)
  
  def save_location(self):
      self.save()

  def update_location(self):
    self.update()

  def delete_location(self):
    self.delete()
  
  def __str__(self):
    return self.title
  
class Category(models.Model):
  image = models.ImageField(upload_to = 'category/')
  url = models.CharField(max_length=48)
  title = models.CharField(max_length=48)
  genus = models.CharField(max_length=200)
  caption = models.TextField(max_length=2000)
  
  def save_category(self):
      self.save()

  def update_category(self):
    self.update()

  def delete_category(self):
    self.delete()
  
  def __str__(self):
    return self.title
  
  class Meta:
    db_table = 'category'
    verbose_name = 'Category List'
  
  
class Cat(models.Model):
  image = models.ImageField(upload_to = 'cats/')
  title = models.CharField(max_length=200)
  caption = models.TextField(max_length=2000)
  posted = models.DateTimeField('date published', default = timezone.now)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  
  def recently_posted(self):
    return self.posted >= timezone.now() - datetime.timedelta(days=1)
  
  def save_cat(self):
    self.save()

  def update_cat(self):
    self.update()

  def delete_cat(self):
    self.delete()
    
  @classmethod
  def search_by_category(cls, search_term):
    cats = cls.objects.filter(category__title__icontains=search_term)
    return cats
     
  def __str__(self):
    return self.title
  