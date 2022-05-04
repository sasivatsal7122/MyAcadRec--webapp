import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import json
import streamlit as st



def run_semester_analytics(username):
    sem_c = st.slider("Select no.of Semesters",1,8,4)
    if sem_c:
        with open(f'user_record/aids/{username}/sem.json','r') as fp:
            main_data = json.load(fp)
            for i in range(1,sem_c+1):
                globals()[f'sem_{i}'] = main_data[username][f'sem{i}']
                globals()[f'sem_{i}_df'] = pd.DataFrame(globals()[f'sem_{i}'])
                if 'Column1' in globals()[f'sem_{i}_df'].columns:
                        globals()[f'sem_{i}_df'].drop(['Column1'],axis=1,inplace=True)
                        
        for i in range(1,sem_c+1):
            
            globals()[f'sem_{i}_df'].drop(globals()[f'sem_{i}_df'].tail(1).index,inplace=True)
            
        
        sem_freq_ls=[]
        sem_freq_ls_2=[]

        for i in range(1,sem_c+1):
            
            globals()[f'sem_{i}_grade_list'] = globals()[f'sem_{i}_df']['Your Grade'].tolist()
            
            globals()[f'all_sem_freqdf_{i}'] = pd.DataFrame({
                                                'Grade':globals()[f'sem_{i}_grade_list'],
                                                'semster':f'sem{i}'
                                            })
            sem_freq_ls.append(globals()[f'all_sem_freqdf_{i}'])
            sem_freq_ls_2.append(f'Semester-{i}')
            
        all_sem_freqdf = pd.DataFrame()
        all_sem_freqdf = pd.concat(sem_freq_ls, 
                        ignore_index = True,axis=0)

        all_sem_freqdf_dict = all_sem_freqdf['Grade'].value_counts().to_dict()
        all_sem_freqdf_values = list(all_sem_freqdf_dict.values())
        all_sem_freqdf_values_sum = sum(all_sem_freqdf_values)
        
        st.header("Basic Stats :")
        st.text('')
        
        grade_dict = {'O':10,'A':9,'B':8,'C':7,'D':6,'F':0}

        for i in range(1,sem_c+1):
            globals()[f'sem_{i}_df']['GradePt'] = (globals()[f'sem_{i}_df']['Your Grade'].map(grade_dict).fillna(0))
            globals()[f'sem_{i}_df']['GradePt'] = globals()[f'sem_{i}_df']['GradePt'].astype(float)
            globals()[f'sem_{i}_df'] = globals()[f'sem_{i}_df'].replace(to_replace ="-",
                            value ="0")
            globals()[f'sem_{i}_df']['Credits'] = globals()[f'sem_{i}_df']['Credits'].astype(float)
            globals()[f'sem_{i}_df']['CreditsMul'] = globals()[f'sem_{i}_df'].Credits * globals()[f'sem_{i}_df'].GradePt
            stud_sgpa_dict= {}
            stud_percentage_dict= {}

            stud_df = globals()[f'sem_{i}_df']

            sem_total_crdits = stud_df['Credits'].sum()
            stud_total_crdits = stud_df['CreditsMul'].sum()
            stud_sgpa = round(stud_total_crdits/sem_total_crdits,4)
            stud_sem_percentage = (stud_sgpa*10)-7.5

            st.subheader(f"You Secured {stud_sgpa} SGPA and {round(stud_sem_percentage,3)}% in Semester-{i}")
            
        st.text('')
        st.text('')
        col1,col2 = st.columns(2)
        with col1:
            for grade in all_sem_freqdf_dict.keys():
                if all_sem_freqdf_dict.get(grade) >1 :
                    st.write(f"out of {all_sem_freqdf_values_sum} subjects You got {all_sem_freqdf_dict.get(grade)} {grade}'s ")
                else:
                    st.write(f"out of {all_sem_freqdf_values_sum} subjects You got {all_sem_freqdf_dict.get(grade)} {grade}'s ")
            
        
        with col2:
            grade_pls=[];grade_cpls = []
            for grade in all_sem_freqdf_dict.keys():    
                percentage = (all_sem_freqdf_dict.get(grade)/all_sem_freqdf_values_sum)*100
                st.write(f"Percentage of {grade}'s' is {round(percentage,4)}%")
                grade_pls.append(grade)
                grade_cpls.append(round(percentage,4))
            
        percentage_df = pd.DataFrame({'grade':grade_pls,'percentage':grade_cpls})
        fig = px.bar(percentage_df, y='percentage', x='grade',text='percentage',width=1000,height=700)
        fig.update_traces(texttemplate='%{text:.5s}%', 
                        textposition='outside')
        fig.update_layout(uniformtext_minsize=8, 
                        uniformtext_mode='hide')
        fig.update_layout(xaxis_fixedrange=True,yaxis_fixedrange=True)
        st.plotly_chart(fig)
        
        all_sem_freqdf_tuple = tuple(sem_freq_ls_2)
        all_sem_freqdf_tuple_main = tuple(sem_freq_ls)
        per_sem = st.radio("Select one semster",all_sem_freqdf_tuple)
        index_tuple = all_sem_freqdf_tuple.index(per_sem)
        fig = px.bar(all_sem_freqdf_tuple_main[index_tuple], x="Grade", color="semster", title="Long-Form Input",width=1000,height=700)
        fig.update_layout(xaxis_fixedrange=True,yaxis_fixedrange=True)
        st.plotly_chart(fig)
        
        fig = px.bar(all_sem_freqdf, x="Grade", color="semster", title="Long-Form Input",width=1000,height=700)
        fig.update_layout(xaxis_fixedrange=True,yaxis_fixedrange=True)
        st.plotly_chart(fig)



    
        