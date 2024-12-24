import streamlit as st
from forms.contact_form import contact_form

@st.dialog('Contact Me')
def show_contact_form():
    contact_form()

st.title('Julian Cangelosi Portfolio')
st.subheader('Welcome to my website!')
st.write(
    """
    Hi there! 
    
    I'm a Computer Science senior, set to graduate in May 2025. With a strong 
    foundation in coding, problem-solving, and a love for creating impactful solutions, 
    I'm eager to take the next step in my journey. I'm currently looking for software 
    engineering positions starting on May 19th, 2025.
    """
)

if st.button('✉️ Contact Me'):
    show_contact_form()