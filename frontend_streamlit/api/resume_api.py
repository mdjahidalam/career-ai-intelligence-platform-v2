import requests

BASE_URL = "http://127.0.0.1:8000"


def get_headers(token):

    return {

        "Authorization": f"Bearer {token}"

    }


# ------------------------------

def upload_resume(token, file):

    files = {

        "file": (

            file.name,

            file,

            "application/pdf"

        )

    }

    return requests.post(

        f"{BASE_URL}/resume/upload",

        headers=get_headers(token),

        files=files

    )


# ------------------------------

def get_resumes(token):

    return requests.get(

        f"{BASE_URL}/resume/",

        headers=get_headers(token)

    )


# ------------------------------

def analyze_resume(token, resume_id):

    return requests.post(

        f"{BASE_URL}/resume/analyze/{resume_id}",

        headers=get_headers(token)

    )


# ------------------------------

def get_dashboard(token, resume_id):

    return requests.get(

        f"{BASE_URL}/resume/dashboard/{resume_id}",

        headers=get_headers(token)

    )


# ------------------------------

def delete_resume(token, resume_id):

    return requests.delete(

        f"{BASE_URL}/resume/{resume_id}",

        headers=get_headers(token)

    )


# ------------------------------

def download_analysis(token, resume_id):

    return requests.get(

        f"{BASE_URL}/resume/download-analysis/{resume_id}",

        headers=get_headers(token)

    )