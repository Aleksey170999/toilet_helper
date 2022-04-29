from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Author, Toilet


class ToiletListView(ListView):
    model = Toilet
    fields = '__all__'
    template_name = 'toiletmodel_list.html'


class ToiletDetailView(DetailView):
    model = Toilet
    fields = '__all__'
    template_name = 'toiletmodel_detail.html'


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiYWxla3NleTE3MDk5OSIsImEiOiJjbDJrMjBteGcwMDBlM2xwY3JnNm9meGxoIn0.emGS4LjHFERQxm82V4yXUg'
    return render(request, 'toilet-map.html',
                  {'mapbox_access_token': mapbox_access_token})