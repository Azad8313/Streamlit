import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Nearest Pubs')
st.title('Find your 5 Nearest Pubs')

df=pd.read_csv(('data\open_pubs1.csv'))

lat=st.number_input("Enter Latitude::")
long=st.number_input('Enter Longitude::')

button_click=st.button('Search')

location=df[['latitude','longitude']]
new_location=np.array([lat,long])

distances = np.sqrt(np.sum((new_location - location)**2, axis = 1))
n = 5
min_indices = np.argpartition(distances,n-1)[:n]

if button_click==True:
    st.markdown("### Nearest Pubs Are")
    st.map(df.iloc[min_indices])