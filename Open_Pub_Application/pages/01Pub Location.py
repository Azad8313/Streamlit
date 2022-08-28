import pandas as pd
import streamlit as st

st.set_page_config(page_title='Pub_location')
st.title('Pub Location')

df=pd.read_csv(('data\open_pubs1.csv'))

option=st.selectbox(
    'Select a Local Authority',
    df['local_authority'].unique()
    )

button_click=st.button('Search')
if button_click==True:
    count=df[df['local_authority']==option]
    # cols =cols[['latitude', 'longitude']]
    st.map(count)
    #st.write(df['local_authority'].value_counts().sort_index())
    # cols=['latitude','longitude']
    # st.map(df[cols])