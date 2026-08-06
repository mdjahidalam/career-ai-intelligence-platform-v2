// ==========================================
// Career AI Configuration
// ==========================================

const API = {

    BASE_URL: "http://127.0.0.1:8000"

};

// ==========================================
// Local Storage
// ==========================================

function saveToken(token) {

    localStorage.setItem(

        "access_token",

        token

    );

}

function getToken() {

    return localStorage.getItem(

        "access_token"

    );

}

function removeToken() {

    localStorage.removeItem(

        "access_token"

    );

}

// ==========================================
// Authorization Header
// ==========================================

function authHeaders() {

    return {

        "Authorization":

            "Bearer " + getToken()

    };

}

// ==========================================
// API Request
// ==========================================

async function apiRequest(

    endpoint,

    options = {}

) {

    const response = await fetch(

        API.BASE_URL + endpoint,

        options

    );

    if (response.status === 401) {

        removeToken();

        window.location.href =

            "login.html";

        return;

    }

    return response;

}