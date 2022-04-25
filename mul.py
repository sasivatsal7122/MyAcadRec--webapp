import streamlit as st
import pickle as pkle
import os.path

pages = ['Page1','Page2','Page3']

if os.path.isfile('next.p'):
    next_clicked = pkle.load(open('next.p', 'rb'))
    if next_clicked == len(pages):
        next_clicked = 0 
else:
    next_clicked = 0 

if next:
    next_clicked = next_clicked+1
    if next_clicked == len(pages):
        next_clicked = 0 

choice = st.sidebar.selectbox("Pages",('Page1','Page2', 'Page3'), index=next_clicked)
pkle.dump(pages.index(choice), open('next.p', 'wb'))

if choice == 'Page1':
    
    st.title('Page 1')
    st.header('sdnflskhjlk')
    st.header('sdnflskhjlk')
    st.header('sdnflskhjlk')
    st.header('sdnflskhjlk')
    st.header('sdnflskhjlk')
    st.header('sdnflskhjlk')
    st.header('sdnflskhjlk')
    st.header('sdnflskhjlk')
    st.header('sdnflskhjlk')
    st.header('sdnflskhjlk')
    st.header('sdnflskhjlk')
elif choice == 'Page2':
    st.title('Page 2')
elif choice == 'Page3':
    st.title('Page 3')
col1,col2,col3 = st.columns([2,2,1])

if choice == 'Page2':
    with col1:
        next = st.button('Go to next page')
if choice == 'Page3':
    with col3:
        next = st.button('Go to next page')
if choice == 'Page1':
    with col2:
        next = st.button('Go to next page')

