
from django.contrib import admin
from django.urls import path, include

from orders.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orders.urls')),
]

handler404 = page_not_found
