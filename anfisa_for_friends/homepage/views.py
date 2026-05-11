from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from ice_cream.models import Category, IceCream


def index(request: HttpRequest) -> HttpResponse:
    template_name = 'homepage/index.html'

    # запрос всех полей таблицы
    # ice_cream_list = IceCream.objects.all()
    # context = {
    #     'ice_cream_list': ice_cream_list,
    # }

    # запрос с фильром и исключением
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
    ).filter(
        is_on_main=True
    ).exclude(
        is_published=False
    ).order_by('title')[1:4]

    categories = Category.objects.values(
        'id', 'output_order', 'title'
    ).order_by(
        # Сортируем записи по значению поля output_order,
        # а если значения output_order у каких-то записей равны —
        # сортируем эти записи по названию в алфавитном порядке
        'output_order', 'title'
    )

    context = {
        'ice_cream_list': ice_cream_list,
        'categories': categories,
    }
    return render(request, template_name, context)
