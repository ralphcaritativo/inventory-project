from django.contrib import admin
from django.urls import path
from products import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name = 'login'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
]
