  
# import the required libraries
import numpy as np  
import pandas as pd  

#%matplotlib inline  

import streamlit as st
import os

import analysis

def main():
    norway_data = analysis.get_data()
    
    #print (norway_data)
    st.table(norway_data)

if __name__ == "__main__":
    main()
