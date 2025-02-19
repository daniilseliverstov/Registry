from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('orders/', views.get_all_orders, name='orders'),
    path('orders/<int:order_id>/', views.order_page, name='order'),
    path('statistics/', views.statistics, name='statistics'),
    path('addorder/', views.add_order, name='add_order'),
    path('login/', views.login, name='login'),

]
