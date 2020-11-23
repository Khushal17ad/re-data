import os
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def convert_location_to_coords(name):
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

    name = name.split(',')[0]
    geolocator = Nominatim(user_agent="Your_Name")
    location = geolocator.geocode(name)

    lat = location.latitude
    long = location.longitude
    return location,lat,long

def get_data():
    norway_data = pd.read_csv('./data/Vindkraftverk.csv',engine='python',error_bad_lines=False, sep = ';')

    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
    norway_data['location'] = norway_data['Fylke(r)'].apply(geocode)
    #norway_data['location'] = norway_data['Fylke(r)'].apply(lambda x: convert_location_to_coords(x))
    return norway_data


