  
# import the required libraries
import numpy as np  
import pandas as pd
import plotly.express as px

#%matplotlib inline  

import streamlit as st
import os

import analysis

def main():

    st.header('Renewable Energy Data')
    st.text("")

    country_option = st.sidebar.selectbox('Select the Country',('All', 'Norway','USA'))

    if country_option == 'Norway':
        norway_data = analysis.get_norway_data()
        
        #st.table(norway_data)

        norway_data = norway_data.sort_values(by = 'avg_annual_prodcution_GWH')
        fig = px.scatter_mapbox(norway_data, lat="lat", lon="lon", hover_name="power_plant_name", hover_data=['main_owner','operational_year','operating_turbines','installed_power_total_MW'],
                            size_max = 10, zoom=3, height=500 ) #color_continuous_scale = px.colors.sequential.Magenta color = 'avg_annual_prodcution_GWH',size = 'year_commissioned',
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.show()

        st.plotly_chart(fig)

        st.subheader('Year-wise comparison of different properties')

        property_option_label_sidebar = st.sidebar.selectbox('Select the property for year wise comparison',('Average Hub Height (in metres)', 'Average Rotor Diameter (in metres)','Total Installed Capacity (in MW)'))

        fig1 = analysis.scatter_plot(property_option_label_sidebar, norway_data)
        st.plotly_chart(fig1)

    elif country_option == 'USA':
        
        us_data = analysis.get_usgs_data()

        #st.table(us_data.head())

        fig = px.scatter_mapbox(us_data, lat="lat", lon="lon", hover_name="county", hover_data=['operational_year','operating_turbines'],
                            size_max = 10, zoom=3, height=500 ) #color_continuous_scale = px.colors.sequential.Magenta color = 'avg_annual_prodcution_GWH',size = 'year_commissioned',
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.show()

        
        st.plotly_chart(fig)

        st.subheader('Year-wise comparison of different properties')

        property_option_label_sidebar = st.sidebar.selectbox('Select the property for year-wise comparison',('Average Hub Height (in metres)', 'Average Rotor Diameter (in metres)','Total Installed Capacity (in MW)'))

        fig1 = analysis.scatter_plot(property_option_label_sidebar, us_data)
        st.plotly_chart(fig1)


    elif country_option == 'All':
        norway_data = analysis.get_norway_data()
        norway_data['country'] = 'Norway'

        us_data = analysis.get_usgs_data()
        us_data['country'] = 'USA'

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

        st.subheader('Country and Year-wise comparison of different properties')

        property_option_label_sidebar = st.sidebar.selectbox('Select the property for year-wise comparison',('Average Hub Height (in metres)', 'Average Rotor Diameter (in metres)','Total Installed Capacity (in MW)')) 

        fig1 = analysis.scatter_plot(property_option_label_sidebar, all_data)
        
        if property_option_label == 'Average Hub Height (in metres)':
            property_option = "avg_hub_height_M"
            fig1 = px.scatter(data_df, x = 'operational_year', y = property_option, color = 'country',labels={
                        "operational_year" : "Operational Year",
                        property_option : property_option_label
                    })
            
        elif property_option_label == 'Average Rotor Diameter (in metres)':
            property_option = "avg_rotor_diameter_M"

            fig1 = px.scatter(data_df, x='operational_year', y=property_option, color = 'country',labels={
                        "operational_year" : "Operational Year",
                        property_option : property_option_label
                    })
        
        else:
            property_option = "installed_power_total_MW"

            fig1 = px.scatter(data_df, x='operational_year', y=property_option, color = 'country',labels={
                        "operational_year" : "Operational Year",
                        property_option : property_option_label
                    })
        
        st.plotly_chart(fig1)

    else:
        pass
if __name__ == "__main__":
    main()
