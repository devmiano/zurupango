from django.shortcuts import render
from .models import Cat, Category

def index(request):
  categories = Category.objects.order_by('-url')
  latest_cats = Cat.objects.order_by('-posted')[:4]
  title = "Visit the Den of Africas' Big Cats"
  template = 'den/index.html'
  
  context = {
    'title': title,
    'categories': categories,
    'latest_cats': latest_cats,
  }
  
  return render(request, template, context)

def detail(request, category_name, cat_id ):
  cat = Cat.objects.filter(id=cat_id).first()
  categories = Category.objects.order_by('-url')
  category = Category.objects.get(url=category_name)
  title = f'{cat.title}'
  template = 'den/detail.html'
  
  if category.id == cat.category:
    category_name = category.url
    
  context = {
    'cat': cat,
    'title': title,
    'categories': categories,
    'category_name': category_name
  }
  
  return render(request, template, context)

def category(request, category_name):
  category = Category.objects.get(url=category_name)
  cat = Cat.objects.filter(category_id=category.id).order_by('-posted').all()
  categories = Category.objects.order_by('-url')
  
  title = f'{category.title}'
  template = 'den/category.html'
  
  if category.id == cat:
    category_name = category.url
  
  context = {
    'cats': cat,
    'title': title,
    'category': category,
    'categories': categories,
  }
  
  return render(request, template, context)