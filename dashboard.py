import streamlit as st
import pandas as pd
from PIL import Image
import json
import os
import os.path
from streamlit_option_menu import option_menu


def Dashboard():
    try:
        f = open('user_creds/temp_login.json')
        log_details = json.load(f)
        username = list(log_details.keys())
        name = list(log_details.values())
    except:
        st.error("You Haven't Logged in...Please Log in and try again...")
    
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
        file_exists = os.path.exists(f'user_record/aids/{username[0]}.json')
        
        if file_exists!=True:
            with open(f'user_record/aids/{username[0]}.json', 'w') as fp:
                pass
        else:
            pass
            
        try:
            with open(f'user_record/aids/{username[0]}.json') as d:
                main_data = json.load(d)
                sem_1 = main_data[username[0]]['sem1']
                sem_2 = main_data[username[0]]['sem2']
                sem_3 = main_data[username[0]]['sem3']
                global sem_1_df,sem_2_df,sem_3_df
                sem_1_df = pd.DataFrame(sem_1)
                if 'Column1' in sem_1_df.columns:
                        sem_1_df.drop(['Column1'],axis=1,inplace=True)
                sem_2_df = pd.DataFrame(sem_2)
                if 'Column1' in sem_2_df.columns:
                        sem_2_df.drop(['Column1'],axis=1,inplace=True)
                sem_3_df = pd.DataFrame(sem_3)
                if 'Column1' in sem_3_df.columns:
                        sem_3_df.drop(['Column1'],axis=1,inplace=True)
        except:
            with open('template/aids/sem1.json') as d:
                sem_1 = json.load(d)
            with open('template/aids/sem2.json') as d:
                sem_2 = json.load(d)
            with open('template/aids/sem3.json') as d:
                sem_3 = json.load(d)
            
            sem_1_df = pd.DataFrame(sem_1)
            if 'Column1' in sem_1_df.columns:
                    sem_1_df.drop(['Column1'],axis=1,inplace=True)
            sem_2_df = pd.DataFrame(sem_2)
            if 'Column1' in sem_2_df.columns:
                    sem_2_df.drop(['Column1'],axis=1,inplace=True)
            sem_3_df = pd.DataFrame(sem_3)
            if 'Column1' in sem_3_df.columns:
                    sem_3_df.drop(['Column1'],axis=1,inplace=True)
        
        def edit_data(semdf,course_title,grade):
            i = semdf.index[semdf['Course Title']==course_title].tolist()
            try:
                semdf.at[i[0],'Your Grade'] = grade
                return semdf
            except:
                return semdf
        
        def save_data():
            super_dict = {};superrr_dict ={}
            for i in range(3):
                xxx = globals()[f'sem_{i+1}_df']
                temporay_dict = xxx.to_dict()
                super_dict.update({f'sem{i+1}':temporay_dict})
            superrr_dict.update({username[0]:super_dict})
            with open(f'user_record/aids/{username[0]}.json', 'w') as fp:
                fp.seek(0)
                json.dump(superrr_dict,fp,indent = 4)
        
        
        
        with st.expander("Semester-1 Record"):
        
            def add_data(sem_df,i):
                grade = st.text_input(f"Enter Your Grade for {row['Course Title']}: ",key='text1').upper()
                sem_df.at[i,'Your Grade'] = grade
                return sem_df
            
            def show(sem_1_df):
                st.dataframe(sem_1_df)
            
            xx = sem_1_df.iloc[1]
            
            if xx['Your Grade']=='-':
                show(sem_1_df)
                for i, row in sem_1_df.iterrows():
                    sem_1_df = add_data(sem_1_df,i)       
            else:
                sub_name = sem_1_df.iloc[1]
                course_title,grade = st.text_input("Course Title and new grade to edit :",f"{sub_name['Course Title']},O",key='edit1').split(',')
                edit_btn = st.button("Edit Changes",key='edit1')
                if edit_btn:
                    sem_1_df = edit_data(sem_1_df,course_title,grade.title())
                save_data()
                st.dataframe(sem_1_df)
            if xx['Your Grade']=='-':
                but_1 = st.button("Save My Data",key='btn1')
                if but_1:
                    st.success("Your Data Has Been Successufully updated")
                    show(sem_1_df)
        
        with st.expander("Semester-2 Record"):
            
            def add_data(sem_df,i):
                grade = st.text_input(f"Enter Your Grade for {row['Course Title']}: ",key='text2').upper()
                sem_df.at[i,'Your Grade'] = grade
                return sem_df
            
            def show(sem_2_df):
                st.dataframe(sem_2_df)
            
            xx = sem_2_df.iloc[1]
            
            if xx['Your Grade']=='-':
                show(sem_2_df)
                for i, row in sem_2_df.iterrows():
                    sem_2_df = add_data(sem_2_df,i)       
            else:
                sub_name = sem_2_df.iloc[1]
                course_title,grade = st.text_input("Course Title and new grade to edit :",f"{sub_name['Course Title']},O",key='edit2').split(',')
                edit_btn = st.button("Edit Changes",key='edit2')
                if edit_btn:
                    sem_2_df = edit_data(sem_2_df,course_title,grade.title())
                save_data()
                st.dataframe(sem_2_df)
            if xx['Your Grade']=='-':
                but_2 = st.button("Save My Data",key='btn2')
                if but_2:
                    st.success("Your Data Has Been Successufully updated")
                    show(sem_2_df)
            
        with st.expander("Semester-3 Record"):
            
            def add_data(sem_df,i):
                grade = st.text_input(f"Enter Your Grade for {row['Course Title']}: ",key='text3').upper()
                sem_df.at[i,'Your Grade'] = grade
                return sem_df
            
            def show(sem_3_df):
                st.dataframe(sem_3_df)            
            
            xx = sem_3_df.iloc[1]
            
            if xx['Your Grade']=='-':
                show(sem_3_df)
                for i, row in sem_1_df.iterrows():
                    sem_3_df = add_data(sem_3_df,i)       
            else:
                sub_name = sem_3_df.iloc[1]
                course_title,grade = st.text_input("Course Title and new grade to edit :",f"{sub_name['Course Title']},O",key='edit3').split(',')
                edit_btn = st.button("Edit Changes",key='edit3')
                if edit_btn:
                    sem_3_df = edit_data(sem_3_df,course_title,grade.title())
                save_data()
                st.dataframe(sem_3_df)
            
            if xx['Your Grade']=='-':
                but_3 = st.button("Save My Data",key='btn3')
                if but_3:
                    st.success("Your Data Has Been Successufully updated")
                    show(sem_3_df)
        
        final_save = st.button("Save My Data in Database",key='finalsave')
        
        if final_save:
            super_dict = {};superrr_dict ={}
            for i in range(3):
                xxx = globals()[f'sem_{i+1}_df']
                temporay_dict = xxx.to_dict()
                super_dict.update({f'sem{i+1}':temporay_dict})
            superrr_dict.update({username[0]:super_dict})
            with open(f'user_record/aids/{username[0]}.json', 'w') as fp:
                fp.seek(0)
                json.dump(superrr_dict,fp,indent = 4)
            st.success("Your Data Has Been Successufully updated in the DataBase")
            st.experimental_rerun()
            

    elif user_option=='Analytics':
        pass
    
    else:
        pass
   
   
        
    
   
        