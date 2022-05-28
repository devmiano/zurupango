from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<category>/', views.base, name='base'),
  path('<category_name>/<int:cat_id>/', views.detail, name='detail'),
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  