import streamlit as st

def contact_form():
    with st.form('contact_form'):
        name = st.text_input('Name')
        email = st.text_input('Email Address')
        phone = st.text_input('Phone Number')
        message = st.text_area('Your Message')
        submit_button = st.form_submit_button('Submit')

        if submit_button:
            st.success('Thanks for submitting your message!')