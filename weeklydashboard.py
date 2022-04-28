import streamlit as st
import pandas as pd
import json


def run_weekly_main(username,name):
    st.info(f"Hey {name[0]} we suggest wide mode for this specific section for better usability and visibility")
    with open(f'user_record/aids/{username[0]}/weekly.json') as d:
            main_data = json.load(d)
            sem_1weekly = main_data[username[0]]['sem1']
            sem_2weekly = main_data[username[0]]['sem2']
            sem_3weekly = main_data[username[0]]['sem3']
            sem_4weekly = main_data[username[0]]['sem4']
            
            global sem_1_weekly_df,sem_2_weekly_df,sem_3_weekly_df,sem_4_weekly_df
            sem_1_weekly_df = pd.DataFrame(sem_1weekly)

            sem_2_weekly_df = pd.DataFrame(sem_2weekly)
            
            sem_3_weekly_df = pd.DataFrame(sem_3weekly)
            
            sem_4_weekly_df = pd.DataFrame(sem_4weekly)
            
        
    def save_weekly_data():
        super_dict = {};superrr_dict = {}
        for i in range(4):
            xxx = globals()[f'sem_{i+1}_weekly_df']
            temporay_dict = xxx.to_dict()
            super_dict.update({f'sem{i+1}':temporay_dict})
        superrr_dict.update({username[0]:super_dict})
        with open(f'user_record/aids/{username[0]}/weekly.json', 'w') as fp:
            fp.seek(0)
            json.dump(superrr_dict,fp,indent = 4)
    
    wdict = {'w1':'Weekly-1','w2':'Weekly-2','w3':'Weekly-3','w4':'Weekly-4','w5':'Weekly-5','w6':'Weekly-6'}
    def edit(df,sub,mid,marks):
        i = df.index[df['Course Title']==sub].tolist()
        try:
            df.at[i[0],wdict.get(mid)] = marks
            return df
        except:
            st.warning("You Entered Wrong Options, Check and Try Again")
            return df
    
    with st.expander("Semester - 1 Weekly Test Record"):
        sub_name = sem_1_weekly_df.iloc[1]
        sub,mid,marks = str(st.text_input("Enter Sub-Name, Weekly - w1 or w2 or...w6, marks : ",f"{sub_name['Course Title']},w1,10",key='weekly-1')).split(',')
        wedit_btn = st.button("Edit Changes",key='weekly-1')
        if wedit_btn:
            try:
                sem_1_weekly_df = edit(sem_1_weekly_df,sub,mid,marks)
            except:
                st.warning("You Entered Wrong Options, Check and Try Again")
            save_weekly_data()
        st.dataframe(sem_1_weekly_df)

    with st.expander("Semester - 2 Weekly Test Record"):
        sub_name = sem_2_weekly_df.iloc[1]
        sub,mid,marks = str(st.text_input("Enter Sub-Name, Weekly - w1 or w2 or...w6, marks : ",f"{sub_name['Course Title']},w1,10",key='weekly-2')).split(',')
        wedit_btn = st.button("Edit Changes",key='weekly-2')
        if wedit_btn:
            try:
                sem_2_weekly_df = edit(sem_2_weekly_df,sub,mid,marks)
            except:
                st.warning("You Entered Wrong Options, Check and Try Again")
            save_weekly_data()
        st.dataframe(sem_2_weekly_df)

    with st.expander("Semester - 3 Weekly Test Record"):
        sub_name = sem_3_weekly_df.iloc[1]
        sub,mid,marks = str(st.text_input("Enter Sub-Name, Weekly - w1 or w2 or...w6, marks : ",f"{sub_name['Course Title']},w1,10",key='weekly-3')).split(',')
        wedit_btn = st.button("Edit Changes",key='weekly-3')
        if wedit_btn:
            try:
                sem_3_weekly_df = edit(sem_3_weekly_df,sub,mid,marks)
            except:
                st.warning("You Entered Wrong Options, Check and Try Again")
            save_weekly_data()
        st.dataframe(sem_3_weekly_df)
        
        
    with st.expander("Semester - 4 Weekly Test Record"):
        sub_name = sem_4_weekly_df.iloc[1]
        sub,mid,marks = str(st.text_input("Enter Sub-Name, Weekly - w1 or w2 or...w6, marks : ",f"{sub_name['Course Title']},w1,10",key='weekly-4')).split(',')
        wedit_btn = st.button("Edit Changes",key='weekly-4')
        if wedit_btn:
            try:
                sem_4_weekly_df = edit(sem_4_weekly_df,sub,mid,marks)
            except:
                st.warning("You Entered Wrong Options, Check and Try Again")
            save_weekly_data()
        st.dataframe(sem_4_weekly_df)
        
    
        
    final_weekly_save = st.button("Save My Data in Database",key='finalweeklysave')
    if final_weekly_save:
        super_dict = {};superrr_dict ={}
        for i in range(4):
            xxx = globals()[f'sem_{i+1}_weekly_df']
            temporay_dict = xxx.to_dict()
            super_dict.update({f'sem{i+1}':temporay_dict})
        superrr_dict.update({username[0]:super_dict})
        with open(f'user_record/aids/{username[0]}/weekly.json', 'w') as fp:
            fp.seek(0)
            json.dump(superrr_dict,fp,indent = 4)
        st.success("Your Data Has Been Successufully updated in the DataBase")