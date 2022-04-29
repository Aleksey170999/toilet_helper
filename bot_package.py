import requests

import requests
from geopy.geocoders import Nominatim

def create_toilet_in_DB(dict):
    geolacator = Nominatim(user_agent="`toilet-bot")
    addr_from_loc = geolacator.reverse(dict['location'])
    response = requests.post("http://127.0.0.1:8000/api/toilets/create/",
                             data={
                                 "user_name": dict['user_name'],
                                 "location": dict['location'],
                                 "description": dict['description'],
                                 "rating": dict['rating'],
                                 "address": addr_from_loc,
                                 "user_tg_id": dict['user_tg_id']
                             })
