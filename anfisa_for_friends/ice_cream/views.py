from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from typing import Any

from ice_cream.models import IceCream


def ice_cream_detail(request: HttpRequest, pk: int | str) -> HttpResponse:
    template = 'ice_cream/detail.html'

    # ice_cream = IceCream.objects.get(pk=pk)
    ice_cream = get_object_or_404(
        # Первый аргумент — QuerySet:
        IceCream.objects.only('title', 'description').filter(is_published=True),
        # Второй аргумент — условие, по которому фильтруются записи из QuerySet:
        pk=pk
    )

    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template, context)


def ice_cream_list(request: HttpRequest) -> HttpResponse:
    template = 'ice_cream/list.html'
    context: dict[Any, Any] = {}
    return render(request, template, context)
