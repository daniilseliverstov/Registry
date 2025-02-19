from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from datetime import datetime


menu = [
    {'title': 'Главная страница', 'url_name': 'home'},
    {'title': 'Заказы', 'url_name': 'orders'},
    {'title': 'Статистика', 'url_name': 'statistics'},
    {'title': 'Создать новый заказ', 'url_name': 'add_order'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'customer': 'НМБ', 'manager': 'manager1', 'order_type': 'к',  'order_number': 'НМБ-24-21к',
     'month': 1, 'week': 4, 'start_date': '23.01.2024', 'status': 'completed',
     'technologist': 'technologist1', 'weight': 20, 'package_count': 8, 'has_mdf': True, 'has_fittings': True,
     'has_glass': False, 'has_cnc': True, 'ldsp_agt_area': 5.0, 'mdf_area': 0.8,
     'edge_04': 23.1, 'edge_2': 3.8, 'edge_1': 5.7, 'total_area': 5.8, 'serial_area': 0, 'portal_area': 0},

    {'id': 2, 'customer': 'СИГ', 'manager': 'manager2', 'order_type': 'лк',  'order_number': 'СИГ-24-10лк',
     'month': 1, 'week': 4, 'start_date': '24.01.2024', 'status': 'in_progress',
     'technologist': 'technologist2', 'weight': 20, 'package_count': 30, 'has_mdf': False, 'has_fittings': True,
     'has_glass': False, 'has_cnc': True, 'ldsp_agt_area': 11.3, 'mdf_area': 0,
     'edge_04': 123.1, 'edge_2': 36.1, 'edge_1': 0, 'total_area': 0, 'serial_area': 14.8, 'portal_area': 0},

    {'id': 3, 'customer': 'НМ', 'manager': 'manager1', 'order_type': 'н',  'order_number': 'НМ-24-10н',
     'month': 1, 'week': 4, 'start_date': '25.01.2024', 'status': 'accepted',
     'technologist': 'technologist3', 'weight': None, 'package_count': None, 'has_mdf': None, 'has_fittings': None,
     'has_glass': None, 'has_cnc': None, 'ldsp_agt_area': None, 'mdf_area': None,
     'edge_04': None, 'edge_2': None, 'edge_1': None, 'total_area': None, 'serial_area': None, 'portal_area': None}
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'orders/index.html', context=data)


def get_all_orders(request):
    """Представление для главной страницы"""
    data = {
        'title': menu[1],
        'menu': menu,
        'orders': data_db,
    }
    return render(request, 'orders/orders.html', context=data)


def order_page(request, order_id):
    return HttpResponse(f'Тут отображение заказа c id = {order_id}')


def statistics(request):
    return HttpResponse(f'Страница статистики')


def add_order(request):
    return HttpResponse(f'Шаблон для создания заказа')


def login(request):
    return HttpResponse(f'Авторизация')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
