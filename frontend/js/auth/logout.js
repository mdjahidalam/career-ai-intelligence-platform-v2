// ==========================================
// Career AI Logout
// ==========================================

document.addEventListener(

    "DOMContentLoaded",

    function () {

        initializeLogout();

    }

);

// ==========================================
// Initialize Logout
// ==========================================

function initializeLogout() {

    // Settings Logout Button

    const logoutButton =

        document.getElementById(

            "logoutButton"

        );

    if (logoutButton) {

        logoutButton.addEventListener(

            "click",

            logout

        );

    }

    // Sidebar Logout

    const sidebarLogout =

        document.getElementById(

            "logoutMenu"

        );

    if (sidebarLogout) {

        sidebarLogout.addEventListener(

            "click",

            function (e) {

                e.preventDefault();

                logout();

            }

        );

    }

}

// ==========================================
// Logout Function
// ==========================================

function logout() {

    const confirmLogout = confirm(

        "Are you sure you want to logout?"

    );

    if (!confirmLogout) {

        return;

    }

    localStorage.removeItem(

        "token"

    );

    localStorage.removeItem(

        "resume_id"

    );

    window.location.href =

        "login.html";

}