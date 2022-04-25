import streamlit as st

if "current" not in st.session_state:

    st.session_state.current = None

if "AAA" not in st.session_state:

    st.session_state.AAA = False

if "BBB" not in st.session_state:

    st.session_state.BBB = False

A = st.button("A")

B = st.button("B")

if A:

    st.session_state.current = "A"

if B:

    st.session_state.current = "B"

if st.session_state.current != None:

    if st.session_state.current == "A":

        st.session_state.AAA = True    

        st.session_state.BBB = False

        st.radio('a',('a','a','a'))

    else:

        st.session_state.BBB = True

        st.session_state.AAA = False

        st.radio('b', ('b','b'))