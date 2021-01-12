  
# import the required libraries
import numpy as np  
import pandas as pd
import plotly.express as px

#%matplotlib inline  

import streamlit as st
import os

import analysis

def main():

    st.header('Energy Data')

    country_option = st.sidebar.selectbox('Select the Country',('All', 'Norway','USA'))

    if country_option == 'Norway':
        norway_data = analysis.get_norway_data()
        
        st.table(norway_data)

        norway_data = norway_data.sort_values(by = 'avg_annual_prodcution_GWH')
        fig = px.scatter_mapbox(norway_data, lat="lat", lon="lon", hover_name="power_plant_name", hover_data=['main_owner','operational_year','operating_turbines'],
                            size_max = 10, zoom=3, height=500 ) #color_continuous_scale = px.colors.sequential.Magenta color = 'avg_annual_prodcution_GWH',size = 'year_commissioned',
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.show()

        st.plotly_chart(fig)

    elif country_option == 'USA':
        us_data = analysis.get_usgs_data()

        st.table(us_data.head())

        fig = px.scatter_mapbox(us_data, lat="lat", lon="lon", hover_name="county", hover_data=['operating_turbines'],
                            size_max = 10, zoom=3, height=500 ) #color_continuous_scale = px.colors.sequential.Magenta color = 'avg_annual_prodcution_GWH',size = 'year_commissioned',
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.show()

        
        st.plotly_chart(fig)


    elif country_option == 'All':
        norway_data = analysis.get_norway_data()
        us_data = analysis.get_usgs_data()

        datasets = [norway_data, us_data]

        all_data = pd.concat(datasets)

        #st.table(all_data.head())
        #st.table(all_data.tail())

        fig = px.scatter_mapbox(all_data, lat="lat", lon="lon", hover_name="county", hover_data=['operating_turbines'],
                            size_max = 10, zoom=1, height=800, width = 800 ) #color_continuous_scale = px.colors.sequential.Magenta color = 'avg_annual_prodcution_GWH',size = 'year_commissioned',
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.show()

        st.plotly_chart(fig)


    else:
        pass
if __name__ == "__main__":
    main()
