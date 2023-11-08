import streamlit as stl
import snowflake.connector

stl.title('My Clothing App')
def get_color_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT color_or_style from catalog_for_website")
        return my_cur.fetchall()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_row = get_fruit_load_list()
my_cnx.close()
fruits_selected=streamlit.select("Pick a sweatsuit colour or style:", list(my_data_row[color_or_style]),['Pink'])
