from django.contrib import admin
from django.urls import path, include
from products import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('accounts/', include('accounts.urls')),
]
