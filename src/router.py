import streamlit as st
from urllib.parse import unquote
import time
def get_route():
    url = st.experimental_get_query_params().get("nav")
    url = url[0] if type(url) == list else url
    route = unquote(url) if url is not None else url
    return route
def redirect(new_route, reload=False):
    if new_route[0] != "/":
        new_route = "/" + new_route
    st.experimental_set_query_params(nav=new_route)
    time.sleep(0.1) 
    if reload:
        st.experimental_rerun()