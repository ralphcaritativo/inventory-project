from django.contrib import admin
from django.urls import path, include
from products import views
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('brands/', include('brands.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
