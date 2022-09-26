import streamlit as st
import pandas as pd

page_bg_color= """
<style>
[data-testid="stAppViewContainer"] {
background-color: #CBDBF1;
}
</style>
"""
st.markdown(page_bg_color,unsafe_allow_html=True)
#st.set_page_config(page_title='Diamond price prediction')
st.title('Welcome to Diamond Price Prediction Application')

st.image("https://wallpaperaccess.com/full/175885.jpg",width=700)


#load dataset
df=pd.read_csv('Dataset\diamonds.csv')
st.markdown('**_Dataset::_**')
st.write(df)

st.markdown('**_There are some basic information about dataset::_**')

#rows & columns
row,column=df.shape
st.write('- There are',row,'rows and',column,'columns')

#columns name
st.write('- Columns name::',df.columns)

#Head and Tail
click=st.selectbox("Select an option",('Head','Tail'))
if click=='Head':
    st.write(df.head())
elif click=='Tail':
    st.write(df.tail())

#Description
st.markdown('- **_Description::_**')
st.write(df.describe())

#Statistics
st.markdown('**_Statistics::_**')
st.write('- Mean::',df.mean())
st.write('- Median::',df.median())
st.write('- Mode::',df.mode())
st.write('- Standard Deviation::',df.std())
st.write('- Veriance::',df.var())
st.write('- Co-veriance::',df.cov())
st.write('- Co-relation::',df.corr())
st.write('- Skewness::',df.skew())

#Ploting
st.markdown('**_Visualization::_**')

click=st.selectbox('Select an option for ploting',('cut','color','clarity'))
if click=='cut':
    st.bar_chart(df['cut'].value_counts())
elif click=='color':
    st.bar_chart(df['color'].value_counts())
elif click=='clarity':
    st.bar_chart(df['clarity'].value_counts())


