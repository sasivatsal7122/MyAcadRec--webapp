import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import login

import json


def Dashboard():
    try:
        f = open('user_creds/temp_login.json')
        log_details = json.load(f)
        username = list(log_details.keys())
        name = list(log_details.values())
        colu1,colu2 = st.columns((1,4))
        with colu1:
            image = Image.open(f'user_dp/{username[0]}.jpg')
            st.image(image)
        with colu2:
            st.title(f"Hello {name[0]}, Whats Poppin?")
    except:
        st.error("You Haven't Logged in...Please Log in and try again...")
   
        