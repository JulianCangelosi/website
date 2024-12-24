import streamlit as st

st.markdown(
    """
    <style>
    .css-1s3b1ll a {
        color: white !important; /* Change navigation link color */
        font-size: 18px;       /* Adjust font size */
        font-weight: bold;     /* Make it bold */
    }
    </style>
    """,
    unsafe_allow_html=True
)

home_page = st.Page(
    page='pages/home.py',
    title='Home Page',
    icon='🏠',
    default=True
)
chess_page = st.Page(
    page='pages/chess.py',
    title='Chess Program',
    icon='♟️',
)
movies_page = st.Page(
    page='pages/movies.py',
    title='Movies Database',
    icon='🎞️',
)
parser_page = st.Page(
    page='pages/parser.py',
    title='Parser',
    icon='🌐',
)

pg = st.navigation(pages=[home_page, chess_page, movies_page, parser_page])

pg.run()
