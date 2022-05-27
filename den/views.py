from django.shortcuts import render
from .models import Cat, Category


def base(request):
  categories = Category.objects.order_by('-url')
  context = {
    'categories': categories
  }
  return render(request, 'den/base.html', context)

def index(request):
  categories = Category.objects.order_by('-url')
  latest_cats = Cat.objects.order_by('-posted')[:4]
  context = {
    'categories': categories,
    'latest_cats': latest_cats,
  }
  return render(request, 'den/index.html', context)
