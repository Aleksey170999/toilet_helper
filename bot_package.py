import requests
from geopy.geocoders import Nominatim
from geopy import location


def create_toilet_in_DB(dict):
    geolacator = Nominatim(user_agent="`toilet-bot")
    addr_from_loc = geolacator.reverse(dict['location'])
    dict.update({"address_from_geo": str(addr_from_loc),
                 "author": dict['user_name'],
                 "location": dict['location'],
                 "description": dict['description'],
                 "rating": dict['rating'],
                 "user_tg_id": dict['user_tg_id']
                 })

    response = requests.post("http://127.0.0.1:8000/api/toilets/create/", data=dict)
