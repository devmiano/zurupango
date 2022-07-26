from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('locations/', locations, name='locations'),
    path('dens/<category_name>/', category, name='category'),
    path('locations/<location_name>/', location, name='location'),
    path('cats/<category_name>/<int:cat_id>/', detail, name='detail'),
    path('api/categories/', CategoryListView.as_view()),
    path('api/category/<url>', CategoryDetailView.as_view()),
    path('api/category/<pk>', CategoryIdView.as_view()),
    path('api/locations/', LocationListView.as_view()),
    path('api/location/<url>/', LocationDetailView.as_view()),
    path('api/location/<pk>/', LocationIdView.as_view()),
    path('api/cats/', CatListView.as_view()),
    path('api/cat/<pk>/', CatDetailView.as_view()),
    path('api/search/<search_term>/', SearchCatView.as_view()),
]
