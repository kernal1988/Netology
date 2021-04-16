from csv import DictReader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
from urllib.parse import urlencode


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as file:
        reader = list(DictReader(file))
    paginator = Paginator(reader, 10)
    total_pages = paginator.num_pages
    current_page = int(request.GET.get('page', 1))

    if current_page > total_pages:
        current_page = total_pages
    elif current_page < 1:
        current_page = 1
    page = paginator.get_page(current_page)
    if page.has_next():
        next_page_url = reverse('bus_stations') + '?' \
                        + urlencode({'page': page.next_page_number()})
    else:
        next_page_url = None
    if page.has_previous():
        previous_page_url = reverse('bus_stations') + '?' \
                            + urlencode({'page': page.previous_page_number()})
    else:
        previous_page_url = None
    return render(request, 'index.html', context={
        'bus_stations': page.object_list,
        'current_page': current_page,
        'prev_page_url': previous_page_url,
        'next_page_url': next_page_url,
    })