import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title = 'Dış Ticaret', 
                   page_icon = ':bar_chart:',
                   layout = 'wide'
)

df = pd.read_csv('deneme.csv')[['yr', 'period', 'rgDesc', 'rtTitle', 'ptTitle', 'TradeValue']]

st.sidebar.header('Filtre:')
year = st.sidebar.multiselect(
    'Yıl:',
    options = df['yr'].unique(),
    default = [2020]
)

reporter_country = st.sidebar.multiselect(
    'Reporter Ülke:',
    options = df['rtTitle'].unique(),
    default = ['Turkey']
)

partner_country = st.sidebar.multiselect(
    'Partner Ülke:',
    options = df['ptTitle'].unique(),
    default = df['ptTitle'].unique()
)

df_selection = df.query(
    'yr == @year & rtTitle == @reporter_country & ptTitle == @partner_country'
)

st.dataframe(df_selection)
