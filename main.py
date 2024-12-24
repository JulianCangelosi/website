import streamlit as st
from enum import Enum, auto

class Pages(Enum):
    HOME   = auto()
    CHESS  = auto()
    PARSER = auto()
    MOVIES = auto()

st.sidebar.title("Navigation")
page = st.sidebar.button(
    'Go to:',
    options=list(Pages),
    format_func=lambda x: x.name.replace('_', ' ').title(),
)

if page == Pages.HOME:
    st.title('Home')
elif page == Pages.CHESS:
    st.title('Object-Oriented Chess Program (Python)')
elif page == Pages.PARSER:
    st.title('Generic Language Parser (Golang)')
elif page == Pages.MOVIES:
    st.title('Movies Relational Database')
