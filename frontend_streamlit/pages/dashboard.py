import streamlit as st

from api.resume_api import (
    upload_resume,
    get_resumes,
    analyze_resume,
    delete_resume,
    download_analysis
)

from utils.session import (
    get_token,
    get_user,
    logout
)


def show_dashboard():

    token = get_token()

    user = get_user()

    st.title("🤖 Career AI Platform")

    col1, col2 = st.columns([8,2])

    with col1:

        st.write(

            f"Welcome **{user['full_name']}**"

        )

    with col2:

        if st.button("Logout"):

            logout()

            st.rerun()

    st.divider()

    uploaded_file = st.file_uploader(

        "Upload Resume",

        type=["pdf"]

    )

    if uploaded_file:

        if st.button("Upload Resume"):

            response = upload_resume(

                token,

                uploaded_file

            )

            if response.status_code == 200:

                st.success(

                    "Resume Uploaded Successfully"

                )

                st.rerun()

            else:

                st.error(

                    response.text

                )

    st.divider()

    response = get_resumes(token)

    if response.status_code != 200:

        st.error("Unable to load resumes")

        return

    resumes = response.json()["data"]

    if len(resumes) == 0:

        st.info("No Resume Uploaded")

        return

    st.subheader("My Resume")

    for resume in resumes:

        with st.container(border=True):

            st.write(

                f"📄 {resume['original_filename']}"

            )

            c1, c2, c3 = st.columns(3)

            with c1:

                if st.button(

                    "Analyze",

                    key=f"a{resume['id']}"

                ):

                    analyze_resume(

                        token,

                        resume["id"]

                    )

                    st.rerun()

            with c2:

                if st.button(

                    "Download",

                    key=f"d{resume['id']}"

                ):

                    result = download_analysis(

                        token,

                        resume["id"]

                    )

                    if result.status_code == 200:

                        st.download_button(

                            "Download JSON",

                            result.text,

                            file_name=f"analysis_{resume['id']}.json",

                            mime="application/json"

                        )

            with c3:

                if st.button(

                    "Delete",

                    key=f"x{resume['id']}"

                ):

                    delete_resume(

                        token,

                        resume["id"]

                    )

                    st.rerun()