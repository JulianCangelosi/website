import streamlit as st

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

st.header(':mailbox: Contact me:')

contact_form ="""
<form action="https://formsubmit.co/jcangelosi20@georgefox.edu" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)