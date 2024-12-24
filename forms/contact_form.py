import streamlit as st

with st.form('contact_form'):
    name = st.text_input('Name')
    email = st.text_input('Email Address')
    phone = st.text_input('Phone Number')
    message = st.text_area('Your Message')
    submit_button = st.form_submit_button('Submit')

    if submit_button:
        st.success('Thanks for submitting your message!')



st.header(':mailbox: Contact me:')

contact_form ="""
<form action="https://formsubmit.co/jcangelosi20@georgefox.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)