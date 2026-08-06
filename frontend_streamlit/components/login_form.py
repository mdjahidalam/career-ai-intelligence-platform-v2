import streamlit as st

from api.auth_api import login as api_login
from api.auth_api import get_current_user

from utils.session import login


def show_login():

    st.title("🤖 Career AI Intelligence Platform")

    st.subheader("Sign in to continue")

    email = st.text_input(

        "Email"

    )

    password = st.text_input(

        "Password",

        type="password"

    )

    if st.button(

        "Login",

        use_container_width=True

    ):

        response = api_login(

            email,

            password

        )

        if response.status_code == 200:

            token = response.json()["access_token"]

            user = get_current_user(

                token

            ).json()["data"]

            login(

                token,

                user

            )

            st.rerun()

        else:

            st.error(

                "Invalid Email or Password"

            )