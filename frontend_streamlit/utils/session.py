import streamlit as st


def initialize_session():

    if "token" not in st.session_state:

        st.session_state.token = None

    if "user" not in st.session_state:

        st.session_state.user = None


def login(token, user):

    st.session_state.token = token

    st.session_state.user = user


def logout():

    st.session_state.token = None

    st.session_state.user = None


def is_logged_in():

    return st.session_state.token is not None


def get_token():

    return st.session_state.token


def get_user():

    return st.session_state.user