from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Toilet
from toilet_posts.services import map_marker_detail


class ToiletListView(ListView):
    """
    Выводит список туалетов
    """
    model = Toilet
    fields = '__all__'
    template_name = 'toiletmodel_list.html'


class ToiletDetailView(DetailView):
    """
    Вывыодит детальную информацию о туалете
    """
    model = Toilet
    fields = '__all__'
    template_name = 'toiletmodel_detail.html'

    def get_context_data(self, **kwargs):
        """
        Добавляем контекст для маркеров на карту
        """
        mapbox_access_token = 'pk.eyJ1IjoiYWxlasuki3NleTE3MDk5OSIsImEiOiJjbDJrMjBteGcwMDBlM2xwY3JnNm9meGxoIn0.emGS4LjHFERQxm82V4yXUg'
        context = super(ToiletDetailView, self).get_context_data(**kwargs)
        context['mapbox_access_token'] = mapbox_access_token
        context['map'] = map_marker_detail(context['toilet'])
        return context


def default_map(request):
    """
    Рендерит карту на странице
    """
    mapbox_access_token = 'pk.eyJ1IjoiYWxla3NleTE3MDk5OSIsImEiOiJjbDJrMjBteGcwMDBlM2xwY3JnNm9meGxoIn0.emGS4LjHFERQxm82V4yXUg'
    return render(request, 'toilet-map.html',
                  {'mapbox_access_token': mapbox_access_token})



