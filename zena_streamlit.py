import streamlit as stl
import snowflake.connector

stl.title('My Clothing App')
def get_color_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT color_or_style from catalog_for_website")
        return my_cur.fetchall()
def get_image():
        with my_cnx.cursor(a) as my_cur:
        my_cur.execute("SELECT direct_url from catalog_for_website where color_or_style=a")
        return my_cur.fetchall()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_row = get_color_list()
my_cnx.close()
color_style_selected=stl.select("Pick a sweatsuit colour or style:", list(my_data_row[color_or_style]),['Pink'])

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_url = get_image(color_style_selected)
my_cnx.close()
st.markdown("![Alt Text]("+my_url+")")
