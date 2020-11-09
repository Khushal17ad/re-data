  
# import the required libraries
import numpy as np  
import pandas as pd  


#%matplotlib inline  

import streamlit as st
import os

def main():
    norway_data = pd.read_csv('./data/Vindkraftverk.csv',engine='python',
    error_bad_lines=False)
    
    #print (norway_data)
    st.table(norway_data)

if __name__ == "__main__":
    main()
