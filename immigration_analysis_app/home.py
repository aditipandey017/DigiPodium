import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#config
st.set_page_config(
    layout="wide",
    page_title= "Immigration Analysis App",
    page_icon = "🧊",
)

years = list(range(1980,2014))
cols_to_drop = ['Type', 'Coverage', 'AREA','DEV','REG']
rename_dict = {'OdName':'Country',
                'AreaName':'Continent',
                'RegName':'Region',
                'DevName':'Status'}

def load_data(path):
    df=pd.read_excel('Canada.xlsx', sheet_name=1, skiprows=20, skipfooter=2)   
    df.drop(columns=cols_to_drop, inplace=True)
    df.rename(columns=rename_dict, inplace=True)
    df['Total'] = df[years].sum(axis=1)
    df.set_index('Country', inplace=True)
    return df

with st.spinner('Processing Immigration Data.....'):
    df= load_data('Canada.xlsx')

st.image("https://img.freepik.com/premium-photo/passport-canada-top-satin-canadian-flag_654297-6.jpg", use_column_width=True)
st.title("Immigration Analysis App")
#use video and audio in place of image


total_countries=df.shape[0]
duration="1980-2013"
total_immigrations=df['Total'].sum()
st.header("Data Summary")
c1,c2,c3,c4,c5,c6=st.columns(6)
c1.metric("Total Countries", total_countries)
c2.metric("Years", duration)
c3.metric("Total Immigration", total_immigrations)

st.header("Immigration Visualisation")
fig=px.line(df,x=df.index, y='Total', height=500)
st.plotly_chart(fig, use_container_width=True)

top_countries= df.sort_values(by='Total', ascending=False).head(25)

c1,c2= st.columns([1,3])

limit= c2.slider("Select no. of Countries",1, 25, value=5)
countries= top_countries.index.tolist()[:limit]
countries_df=df.loc[countries,years].T
fig2= px.area(countries_df, x= countries_df.index, y= countries_df.columns)

c1.dataframe(top_countries)
c2.plotly_chart(fig2, use_container_width=True)

st.subheader("Trend Comparison")
c1,c2=st.columns(2)
country_list= df.index.tolist()
countries= c2.multiselect("select Countries", country_list)
if countries:
    countries_df= df.loc[countries, years].T
    fig3= px.line(
        countries_df,
        x= countries_df.index,
        y= countries_df.columns
    )
    for country in countries:
        c1.info(f'{country}:{df.loc[country, "Total"]}Immigrations')
    c2.plotly_chart(fig3,use_container_width=True)
    st.toast('Your Graph has been loaded!', icon='😍')