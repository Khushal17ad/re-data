  
# import the required libraries
import numpy as np  
import pandas as pd
import plotly.express as px

#%matplotlib inline  

import streamlit as st
import os

import analysis

def main():
    norway_data = analysis.get_data()
    
    #print (norway_data)
    st.table(norway_data)

    fig = px.scatter_mapbox(norway_data, lat="lat", lon="lon", hover_name="Fylke(r)", hover_data=["Kraftverksnavn"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300, size_max = 10)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
