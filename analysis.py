import os
import pandas as pd
from geopy.geocoders import Nominatim


def convert_location_to_coords(name):

    name = name.split(',')[0]
    geolocator = Nominatim(user_agent="Your_Name")
    location = geolocator.geocode(name)

    lat = location.latitude
    long = location.longitude
    return location,lat,long

def get_data():
    norway_data = pd.read_csv('./data/Vindkraftverk.csv',engine='python',error_bad_lines=False, sep = ';')

    norway_data['location'] = norway_data['Fylke(r)'].apply(lambda x: convert_location_to_coords(x))
    return norway_data


