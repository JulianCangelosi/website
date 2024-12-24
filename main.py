import streamlit as st

st.title('Julian Cangelosi')


st.button('Hello')
st.sidebar.title("Sidebar Menu")
st.sidebar.radio('Choose an option:', ['Option1', 'Option2', 'Option3'])
st.sidebar.slider('Select a range', 0, 100, 50)