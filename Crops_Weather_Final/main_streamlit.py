from os import curdir
import sqlite3
from sqlite3.dbapi2 import Cursor
import datetime
from datetime import datetime, date
from time import sleep
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
from PIL import Image
from noaa_weather_api import weather_data_pandas_frame
from noaa_weather_api import get_noaa_weather
from plants_treatments_database import plant_db_spin_up
from plants_treatments_database import plant_Update_process
from plants_treatments_database import crops_stream_SQL_Output
from plants_treatments_database import Epsom_Update_button
from plants_treatments_database import Neem_Oil_Update_button
from plants_treatments_database import Fertilizer_Update_button
from plants_treatments_database import Neem_Oil_result
from plants_treatments_database import Epsom_Salt_result
from plants_treatments_database import Fertilizer_result

plant_db_spin_up()

###Browser Tab Properties
st.set_page_config(page_title="Planting and Weather", page_icon=":herb:", layout="wide")
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

###Refresh every 60 Minutes
st_autorefresh(interval=60 * 60 * 1000, key="dataframerefresh")

###Section for tracking fertilizer and other applications in the garden
with st.empty():
    col7, col8, col9 = st.columns(3)
    with col7:
        st.empty()
    with col8:
        st.subheader("Crop Planting & Weather Dashboard")
    with col9:
        st.empty()
with st.empty():
    col4, col5, col6 = st.columns(3)
    with col4:
        neem_df = pd.DataFrame(Neem_Oil_result())
        neem_result = st.button('Neem Oil Applied')
        if neem_result == True:
            Neem_Oil_Update_button()
            neem_updated_df = pd.DataFrame(Neem_Oil_result())
            st.write(neem_updated_df.iloc[0, 0])
            neem_result = False
        else:
            st.write(neem_df.iloc[0, 0])
    with col5:
        epsom_df = pd.DataFrame(Epsom_Salt_result())
        epsom_result = st.button('Epsom Salt Applied')
        if epsom_result == True:
            Epsom_Update_button()
            epsom_updated_df = pd.DataFrame(Epsom_Salt_result())
            st.write(epsom_updated_df.iloc[0, 0])
            epsom_result = False
        else:
            st.write(epsom_df.iloc[0, 0])
    with col6:
        fertilizer_df = pd.DataFrame(Fertilizer_result())
        fertilizer_result = st.button('Fertilizer Applied')
        if fertilizer_result == True:
            Fertilizer_Update_button()
            fertilizer_updated_df = pd.DataFrame(Fertilizer_result())
            st.write(fertilizer_updated_df.iloc[0, 0])
            fertilizer_result = False
        else:
            st.write(fertilizer_df.iloc[0, 0])
###Section for planting schedule and weather data
with st.empty():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Planting Schedule")
        crop_df = pd.DataFrame(crops_stream_SQL_Output(), columns =['Crop', 'Planting Start', 'Planting End'])
        st.dataframe(crop_df, 1400,600)
    with col2:
        st.header("Hourly Weather")
        st.dataframe(get_noaa_weather().style.highlight_max(color='red',subset='Temperature'))
    with col3:
        rain_image = Image.open('weather_frog_rain.png')
        normal_image = Image.open('weather_frog_normal.png')
        curr_forecast_df = get_noaa_weather()
        forecast_text = str(curr_forecast_df.iloc[0, 2])
        lower_forecast_text = str.lower(forecast_text)
        st.header(forecast_text)
        if ("rain" in lower_forecast_text) or ("storm" in lower_forecast_text):
            st.image(rain_image)
        else: 
            st.image(normal_image)


            
