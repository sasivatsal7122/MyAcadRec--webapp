import streamlit as st
import pandas as pd
from PIL import Image
import json
import os
import os.path
from streamlit_option_menu import option_menu

# LOCAL IMPORTS

import middashboard
import semdashbord
import weeklydashboard
import planner

def Dashboard():
    
    logcondition = False

    try:
        f = open('user_creds/temp_login.json')
        log_details = json.load(f)
        username = list(log_details.keys())
        name = list(log_details.values())
        logcondition = True
    except:
        st.error("You Haven't Logged in...Please Log in and try again...")
    
    if logcondition:
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
            
            user_option = st.selectbox("Select  One of the following :  ",("Semster", "Mid Term","Weekly"), 
            key='sasi')
            
            st.text("")
            st.text("")
            
            if user_option=='Semster':
                semdashbord.run_sem_main(username)
                
            elif user_option=='Mid Term':
                middashboard.run_mid_main(username)
                    
            
            elif user_option=='Weekly':
                weeklydashboard.run_weekly_main(username,name)
            
            
        elif user_option=='Analytics':
            pass
        
        else:
            #pass
            planner.run_plannerapp()
    
    else:
        pass
   
   
        
    
   
        