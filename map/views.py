from django.shortcuts import render
from toilet_posts.models import Toilet
from toilet_posts.services import map_markers, map_marker_detail


def map_view_all_markers(request):
    addresses = []
    toilets = Toilet.objects.filter(confirmed__exact=True).values_list()

    for toilet in toilets:
        addresses.append(toilet)
    context = {
        'map': map_markers(addresses),
    }
    return render(request, "toilet-map.html", context)


def map_view_detail(request, pk):
    address = Toilet.objects.get(id=pk)
    print(address)
    context = {
        'map': map_marker_detail(address),
    }
    return render(request, 'toilet_map_detail.html', context)