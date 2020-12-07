  
# import the required libraries
import numpy as np  
import pandas as pd
import plotly.express as px

#%matplotlib inline  

import streamlit as st
import os

import analysis

def main():
    norway_data = analysis.get_data_old()
    
    #print (norway_data)
    st.table(norway_data)

    fig = px.scatter_mapbox(norway_data, lat="lat", lon="lon", hover_name="kommune", hover_data=['year_commissioned'],color = 'avg_annual_prodcution_GWH',
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=3, height=300, size_max = 10)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
