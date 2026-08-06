// ==========================================
// Career AI Settings
// ==========================================

document.addEventListener(

    "DOMContentLoaded",

    function () {

        initializeSettings();

    }

);

// ==========================================
// Initialize
// ==========================================

function initializeSettings() {

    checkAPIStatus();

    setupTheme();

}

// ==========================================
// API Status
// ==========================================

async function checkAPIStatus() {

    try {

        const response = await fetch(

            API.BASE_URL + "/health"

        );

        document.getElementById(

            "apiStatus"

        ).innerHTML =

            response.ok ? "🟢 Online" : "🔴 Offline";

    }

    catch {

        document.getElementById(

            "apiStatus"

        ).innerHTML =

            "🔴 Offline";

    }

}

// ==========================================
// Theme
// ==========================================
function setupTheme(){

    const button = document.getElementById(

        "themeButton"

    );

    if(!button){

        return;

    }

    // Previous theme

    if(

        localStorage.getItem(

            "theme"

        ) === "dark"

    ){

        document.body.classList.add(

            "dark"

        );

        button.innerHTML =

            "☀️ Light Mode";

    }

    button.addEventListener(

        "click",

        function(){

            document.body.classList.toggle(

                "dark"

            );

            if(

                document.body.classList.contains(

                    "dark"

                )

            ){

                localStorage.setItem(

                    "theme",

                    "dark"

                );

                button.innerHTML =

                    "☀️ Light Mode";

            }

            else{

                localStorage.setItem(

                    "theme",

                    "light"

                );

                button.innerHTML =

                    "🌙 Dark Mode";

            }

        }

    );

}