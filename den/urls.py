from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('/search', views.search, name='search'),
  path('dens/<category_name>/', views.category, name='category'),
  path('locations/<location_name>/', views.location, name='location'),
  path('cats/<category_name>/<int:cat_id>/', views.detail, name='detail'),
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  