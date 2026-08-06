import streamlit as st

from utils.session import (
    initialize_session,
    is_logged_in
)

from components.login_form import show_login

st.set_page_config(

    page_title="Career AI Platform",

    page_icon="🤖",

    layout="wide"

)

initialize_session()

if not is_logged_in():

    show_login()

else:

    user = st.session_state.user

    from pages.dashboard import show_dashboard

    show_dashboard()

    