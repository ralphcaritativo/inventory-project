from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.list_products, name = 'list_products'),
    path('create', views.create_product, name = 'create_product'),
    path('update/<int:id>', views.update_product, name = 'update_product'),
]
