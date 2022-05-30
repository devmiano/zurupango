from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('search/', views.search, name='search'),
  path('locations/', views.locations, name='locations'),
  path('dens/<category_name>/', views.category, name='category'),
  path('locations/<location_name>/', views.location, name='location'),
  path('cats/<category_name>/<int:cat_id>/', views.detail, name='detail'),
]
  