import streamlit as stl
import pandas as pd
import snowflake.connector

stl.title('My Clothing App')
def get_color_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT color_or_style from catalog_for_website")
        return my_cur.fetchall()
def get_image(a):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT direct_url from catalog_for_website where color_or_style='"+a+"'")
        return my_cur.fetchall()
my_cnx = snowflake.connector.connect(**stl.secrets["snowflake"])
my_data_row = pd.DataFrame(get_color_list())
my_cnx.close()
color_style_selected=stl.selectbox("Pick a sweatsuit colour or style:", my_data_row)

my_cnx = snowflake.connector.connect(**stl.secrets["snowflake"])
my_url = pd.DataFrame(get_image(color_style_selected))
my_cnx.close()

stl.markdown("![Alt Text]("+my_url[0][0]+")")
