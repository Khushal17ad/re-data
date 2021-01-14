import os
import pandas as pd
import requests
import plotly.express as px
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
    
    norway_data.reset_index(inplace=True)

    column_names = ['power_plant_name','year_commissioned','installed_power_total_MW','main_owner','owner_org_number','county',
                'kommune','avg_annual_prodcution_GWH','avg_generation_power_MW','avg_hub_height_M','avg_rotor_diameter_M',
                'energy_per_swept_area_KWH_m2','operating_turbines','random','location','point','lat','lon']

    
    norway_data.columns = column_names

    norway_data['avg_annual_prodcution_GWH'] = norway_data['avg_annual_prodcution_GWH'].apply(lambda x : x if x else 20)

    #norway_data[['latitude', 'longitude', 'altitude']] = pd.DataFrame(norway_data['point'].tolist()) #, index=norway_data.index
    #norway_data['location'] = norway_data['Fylke(r)'].apply(lambda x: convert_location_to_coords(x))
    #pd.to_csv('norway_edited_data.csv')

    return norway_data

def get_norway_data():
    norway_data = pd.read_csv('./data/norway_data.csv',engine='python',error_bad_lines=False, sep = ',')

    #norway_data.reset_index(inplace=True)

    column_names = ['power_plant_name','operational_year','installed_power_total_MW','main_owner','owner_org_number','county',
                'kommune','avg_annual_prodcution_GWH','avg_generation_power_MW','avg_hub_height_M','avg_rotor_diameter_M',
                'energy_per_swept_area_KWH_m2','operating_turbines','random','location','point','lat','lon']

    print (norway_data.columns)
    norway_data.columns = column_names

    return norway_data

def get_usgs_data():
    us_data = requests.get('https://eersc.usgs.gov/api/uswtdb/v1/turbines?&p_year=gt.1980').json()

    us_data_df = pd.DataFrame(us_data)

    us_data_df.rename(columns = {'t_county' : 'county', 
                                    'xlong':'lon', 
                                    'ylat':'lat',
                                    't_state' : 'state',
                                    'p_name' : 'power_plant_name',
                                    'p_year' : 'operational_year',
                                    'p_tnum' : 'operating_turbines',
                                    'p_cap' : 'installed_power_total_MW',
                                    't_manu' : 'turbine_manufacturer',
                                    't_model' : 'turbine_model',
                                    't_hh' : 'avg_hub_height_M',
                                    't_rd' : 'avg_rotor_diameter_M',
                                    't_rsa' : 'rotor swept area m2',
                                    't_ttlh' : 'turbine_total_height',



                        },inplace=True)

    return us_data_df

def scatter_plot(property_option_label):
    if property_option_label == 'Average Hub Height (in metres)':
            property_option = "avg_hub_height_M"
            fig1 = px.scatter(norway_data, x = 'operational_year', y = property_option, labels={
                        "operational_year" : "Operational Year",
                        property_option : property_option_label
                    })
            
    else:
        property_option = "avg_rotor_diameter_M"

        fig1 = px.scatter(norway_data, x='operational_year', y=property_option, labels={
                    "operational_year" : "Operational Year",
                    property_option : property_option_label
                })
    
    return fig1
