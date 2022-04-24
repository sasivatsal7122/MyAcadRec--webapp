import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import json
from streamlit_option_menu import option_menu


def Dashboard():
    try:
        f = open('user_creds/temp_login.json')
        log_details = json.load(f)
        username = list(log_details.keys())
        name = list(log_details.values())
        col1, col2 = st.columns([1,2])
        with col1:
            image = Image.open(f'user_dp/{username[0]}.jpg')
            st.image(image)
        with col2:
            st.title(f"Hello {name[0]}, Whats Poppin?")
            
       
        user_option = option_menu(None, ["Dashboard", "Analytics","To-DO"], 
        icons=['list', 'graph-up','check2-square'], 
        menu_icon="cast", default_index=0, orientation="horizontal")
        if user_option=='Dashboard':
            pass
        
        elif user_option=='Analytics':
            pass
        
        else:
            pass
            
        
    except:
        st.error("You Haven't Logged in...Please Log in and try again...")
   
        