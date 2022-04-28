import streamlit as st
import pandas as pd
import json

def run_mid_main(username):
    with open(f'user_record/aids/{username[0]}/midterm.json') as d:
        main_data = json.load(d)
        sem_1mid = main_data[username[0]]['sem1']
        sem_2mid = main_data[username[0]]['sem2']
        sem_3mid = main_data[username[0]]['sem3']
        sem_4mid = main_data[username[0]]['sem4']
        
        global sem_1_mid_df,sem_2_mid_df,sem_3_mid_df,sem_4_mid_df
        sem_1_mid_df = pd.DataFrame(sem_1mid)
        
        sem_2_mid_df = pd.DataFrame(sem_2mid)
        
        sem_3_mid_df = pd.DataFrame(sem_3mid)
        
        sem_4_mid_df = pd.DataFrame(sem_4mid)
    
    
    def save_mid_data():
        super_dict = {};superrr_dict ={}
        for i in range(4):
            xxx = globals()[f'sem_{i+1}_mid_df']
            temporay_dict = xxx.to_dict()
            super_dict.update({f'sem{i+1}':temporay_dict})
        superrr_dict.update({username[0]:super_dict})
        with open(f'user_record/aids/{username[0]}/midterm.json', 'w') as fp:
            fp.seek(0)
            json.dump(superrr_dict,fp,indent = 4)
    
    mdict = {'m1':'Mid-Term-1','m2':'Mid-Term-2'}
    def edit(df,sub,mid,marks):
        i = df.index[df['Course Title']==sub].tolist()
        try:
            df.at[i[0],mdict.get(mid)] = marks
            return df
        except:
            st.warning("You Entered Wrong Options, Check and Try Again")
            return df

            
    with st.expander("Semester - 1 Mid-term Record"):
        sub_name = sem_1_mid_df.iloc[1]
        sub,mid,marks = str(st.text_input("Enter Sub-Name, Mid - m1 or m2, marks : ",f"{sub_name['Course Title']},m1,18",key='midds-2')).split(',')
        medit_btn = st.button("Edit Changes",key='mids-1')
        if medit_btn:
            try:
                sem_1_mid_df = edit(sem_1_mid_df,sub,mid,marks)
            except:
                st.warning("You Entered Wrong Option, check and try again ")
            save_mid_data()
        st.dataframe(sem_1_mid_df)
    
    with st.expander("Semester - 2 Mid-term Record"):
        sub_name = sem_2_mid_df.iloc[1]
        sub,mid,marks = str(st.text_input("Enter Sub-Name, Mid - m1 or m2, marks : ",f"{sub_name['Course Title']},m1,18",key='midds-2')).split(',')
        medit_btn = st.button("Edit Changes",key='mids-2')
        if medit_btn:
            sem_2_mid_df = edit(sem_2_mid_df,sub,mid,marks)
            save_mid_data()
        st.dataframe(sem_2_mid_df)
    
    with st.expander("Semester - 3 Mid-term Record"):
        sub_name = sem_3_mid_df.iloc[1]
        sub,mid,marks = str(st.text_input("Enter Sub-Name, Mid - m1 or m2, marks : ",f"{sub_name['Course Title']},m1,18",key='midds-3')).split(',')
        medit_btn = st.button("Edit Changes",key='mids-3')
        if medit_btn:
            sem_3_mid_df = edit(sem_3_mid_df,sub,mid,marks)
            save_mid_data()
        st.dataframe(sem_3_mid_df)
        
        
    with st.expander("Semester - 4 Mid-term Record"):
        sub_name = sem_4_mid_df.iloc[1]
        sub,mid,marks = str(st.text_input("Enter Sub-Name, Mid - m1 or m2, marks : ",f"{sub_name['Course Title']},m1,18",key='midds-4')).split(',')
        medit_btn = st.button("Edit Changes",key='mids-4')
        if medit_btn:
            try:
                sem_4_mid_df = edit(sem_4_mid_df,sub,mid,marks)
            except:
                st.warning("You Entered Wrong Option, Check and Try again")
            save_mid_data()
        st.dataframe(sem_4_mid_df)    
    
    
    final_mid_save = st.button("Save My Data in Database",key='finalmidsave')
    if final_mid_save:
        super_dict = {};superrr_dict ={}
        for i in range(4):
            xxx = globals()[f'sem_{i+1}_mid_df']
            temporay_dict = xxx.to_dict()
            super_dict.update({f'sem{i+1}':temporay_dict})
        superrr_dict.update({username[0]:super_dict})
        with open(f'user_record/aids/{username[0]}/midterm.json', 'w') as fp:
            fp.seek(0)
            json.dump(superrr_dict,fp,indent = 4)
        st.success("Your Data Has Been Successufully updated in the DataBase")
        