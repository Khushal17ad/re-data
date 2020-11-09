  
# import the required libraries
import numpy as np  
import pandas as pd  


#%matplotlib inline  

import streamlit as st

import os

import analysis

def main():
    norway_data = pd.read_csv('./data/Vindkraftverk.csv')

    st.dataframe(norway_data)

if __name__ == "__main__":
    main()
