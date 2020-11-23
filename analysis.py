import os
import pandas as pd
from geopy.geocoders import Nominatim


def convert_location_to_coords(name):
    location = geolocator.geocode(name)
    return location.latitude, location.longitude

def get_data():
    norway_data = pd.read_csv('./data/Vindkraftverk.csv',engine='python',error_bad_lines=False, sep = ';')

    geolocator = Nominatim(user_agent="Your_Name")
    norway_data['location'] = norway_data['Fylke(r)'].apply(lamda x: convert_location_to_coords(x))
    return norway_data


