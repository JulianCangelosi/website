import streamlit as st
import re
import requests

WEBHOOK_URL = 'https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZmMDYzMzA0MzA1MjY5NTUzYzUxMzAi_pc'

def is_valid_email(email: str) -> bool:
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form('contact_form'):
        name = st.text_input('Name')
        email = st.text_input('Email Address')
        phone = st.text_input('Phone Number')
        message = st.text_area('Your Message')
        submit_button = st.form_submit_button('Submit')

        if submit_button:
            if not WEBHOOK_URL:
                st.error('Webhook URL is not set up. Please try again later.')
                st.stop()
            if not name:
                st.error('Please enter your name.')
                st.stop()
            if not email:
                st.error('Please enter your email address.')
                st.stop()
            if not is_valid_email(email):
                st.error('Please enter a valid email address.')
                st.stop()
            if not message:
                st.error('Please enter a message.')
                st.stop()

            data = {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message
            }
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success('Your message has been sent!')
            else:
                st.error('There was an error sending your message.')