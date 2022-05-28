from django.shortcuts import render
from .models import Cat, Category

def base(request, category):
  categories = Category.objects.order_by('-url')
  template = 'den/base.html'
  
  context = {
    'category': category,
    'categories': categories,
  }
  
  return render(request, template, context)

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
