import requests
from geopy.geocoders import Nominatim
from toilets import settings as s


def get_addres_by_location(location):
    geolacator = Nominatim(user_agent="`toilet-bot")
    return geolacator.reverse(location)


def create_toilet_in_DB(dict):
    print(type(dict['location']))

    print(dict['location'])
    addr_from_loc = get_addres_by_location(dict['location'])
    dict.update({"address_from_geo": str(addr_from_loc),
                 "author": dict['user_name'],
                 "location": dict['location'],
                 "description": dict['description'],
                 "rating": dict['rating'],
                 "user_tg_id": dict['user_tg_id'],
                 })
    if s.DEBUG:
        response = requests.post("http://127.0.0.1:8000/api/toilets/create/", data=dict)

    else:
        response = requests.post("https://toilet-helper.herokuapp.com/api/toilets/create/", data=dict)


def dist_between_two_lat_lon(*args):
    from math import asin, cos, radians, sin, sqrt
    lat1, lat2, long1, long2 = map(radians, args)

    dist_lats = abs(lat2 - lat1)
    dist_longs = abs(long2 - long1)
    a = sin(dist_lats / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dist_longs / 2) ** 2
    c = asin(sqrt(a)) * 2
    radius_earth = 6378  # the "Earth radius" R varies from 6356.752 km at the poles to 6378.137 km at the equator.
    return c * radius_earth


def find_closest_lat_lon(data, v):
    return min(data, key=lambda p: dist_between_two_lat_lon(v['lat'], p['lat'], v['lon'], p['lon']))


def find_loc_to_answer(data):
    if s.DEBUG:
        get_response = requests.get(f"http://127.0.0.1:8000/api/toilets/list/")
    else:
        get_response = requests.get(f"https://toilet-helper.herokuapp.com/api/toilets/list/")

    list_of_locs = []
    data_list = []

    for toilet in get_response.json():
        list_of_locs.append(toilet['location'])

    for el in list_of_locs:
        el = el.split(', ')
        for l in range(1):
            a = {'lat': float(el[0]), 'lon': float(el[1])}
            data_list.append(a)
    return find_closest_lat_lon(data_list, data['location'])
