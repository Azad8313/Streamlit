import streamlit as st
import pandas as pd

st.set_page_config(page_title='Open_Pub_Application')
st.title('Welcome to Open Pub Application')

df=pd.read_csv('data\open_pubs1.csv')
st.markdown('**_Dataset::_**')
st.write(df)
#rows & columns
row,column=df.shape
st.write('- There are',row,'rows and',column,'columns')
#Head
st.write('- Head of the dataset')
st.write(df.head())
#columns name
st.write('- Columns name::',df.columns)
#describe the numerical column
st.write('- Describe the dataset::', df.describe())
#Statistics
st.markdown('Statistics::')
cols=['latitude','longitude']
st.write('- Mean::',df[cols].mean())
st.write('- Median::',df[cols].median())
st.write('- Mode::',df[cols].mode())
st.write('- Standard Deviation::',df[cols].std())
st.write('- Veriance::',df[cols].var())
st.write('- Skewness::',df[cols].skew())

