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

def get_data_old():
    norway_data = pd.read_csv('./data/Vindkraftverk.csv',engine='python',error_bad_lines=False, sep = ';')

    geolocator = Nominatim(user_agent="Your_Name")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    
    norway_data['Fylke(r)'] = norway_data['Fylke(r)'].apply(lambda x : x.split(',')[0])
    norway_data['location'] = norway_data['Fylke(r)'].apply(geocode)

    norway_data['point'] = norway_data['location'].apply(lambda loc: tuple(loc.point) if loc else None)

    norway_data['lat'] = norway_data['point'].apply(lambda x : x[0] if x else None)
    norway_data['lon'] = norway_data['point'].apply(lambda x : x[1] if x else None)
    #norway_data[['latitude', 'longitude', 'altitude']] = pd.DataFrame(norway_data['point'].tolist()) #, index=norway_data.index
    #norway_data['location'] = norway_data['Fylke(r)'].apply(lambda x: convert_location_to_coords(x))
    #pd.to_csv('norway_edited_data.csv')

    return norway_data

def get_data():
    norway_data = pd.read_csv('./data/norway_edited_data.csv',engine='python',error_bad_lines=False, sep = ';')

    return norway_data


