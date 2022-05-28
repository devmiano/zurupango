from django.shortcuts import render
from .models import Cat, Category, Location

def index(request):
  categories = Category.objects.order_by('-url')
  locations = Location.objects.order_by('-url')
  latest_cats = Cat.objects.order_by('-posted')[:8]
  title = "Visit the Den of Africas' Big Cats"
  template = 'den/index.html'
  
  context = {
    'title': title,
    'locations': locations,
    'categories': categories,
    'latest_cats': latest_cats,
  }
  
  return render(request, template, context)

def detail(request, category_name, cat_id ):
  cat = Cat.objects.filter(id=cat_id).first()
  categories = Category.objects.order_by('-url')
  category = Category.objects.get(url=category_name)
  locations = Location.objects.order_by('-url')
  title = f'{cat.title}'
  template = 'den/detail.html'
  
  if category.id == cat.category:
    category_name = category.url
    
  context = {
    'cat': cat,
    'title': title,
    'locations': locations,
    'categories': categories,
    'category_name': category_name
  }
  
  return render(request, template, context)

def category(request, category_name):
  category = Category.objects.get(url=category_name)
  cats_by_category = Cat.objects.filter(category_id=category.id).order_by('-posted')
  categories = Category.objects.order_by('-url')
  locations = Location.objects.order_by('-url')
  
  title = f'{category.title}: {category.genus}'
  template = 'den/category.html'
  
  if category.id == cats_by_category:
    category_name = category.url
  
  context = {
    'title': title,
    'category': category,
    'locations': locations,
    'categories': categories,
    'cats': cats_by_category,
  }
  
  return render(request, template, context)

def location(request, location_name):
  location = Location.objects.get(url=location_name)
  cats_by_location = Cat.objects.filter(location_id=location.id).order_by('-posted')
  locations = Location.objects.order_by('-url')
  categories = Category.objects.order_by('-url')
  
  title = f'{location.title}'
  template = 'den/location.html'
  
  if location.id == cats_by_location:
    location_name = location.url
    
  context = {
    'title': title,
    'location': location,
    'locations': locations,
    'categories': categories,
    'cats': cats_by_location,
  }
  
  return render(request, template, context)

