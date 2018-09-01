from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.list_brands, name = 'list_brands'),
    path('create', views.create_brand, name = 'brand_form'),
    path('<int:id>/update', views.update_brand, name = 'update_brand'),

]
