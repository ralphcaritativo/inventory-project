from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.list_category, name = 'list_category'),
    path('create', views.create_category, name = 'category_form'),
    path('<int:id>/update', views.update_category, name = 'update_category'),

]
