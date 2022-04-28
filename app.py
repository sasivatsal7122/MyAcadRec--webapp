import streamlit as st
import login
import dashboard

st.set_page_config(page_title="My Acad Record - VIIT",page_icon='📚')
st.sidebar.subheader("Navigation Menu")
choice = st.sidebar.selectbox('Choose Dashboard after login',
     ('Login', 'My Dashboard'))
sasi=''
if choice=='Login':
   login.main()
else:
    dashboard.Dashboard()