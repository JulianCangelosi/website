import streamlit as st

home_page = st.Page(
    page='pages/home.py',
    title='Home Page',
    icon=':material/account_circle',
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
    icon=':materials/language',
)

pg = st.navigation(pages=[home_page, chess_page, movies_page, parser_page])

pg.run()
