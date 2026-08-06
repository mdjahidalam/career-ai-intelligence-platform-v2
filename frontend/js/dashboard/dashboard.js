// ==========================================
// Career AI Dashboard
// ==========================================

// ==========================================
// Authentication Check
// ==========================================

if (!getToken()) {

    window.location.href = "login.html";

}

// ==========================================
// Dashboard Initialize
// ==========================================

document.addEventListener(

    "DOMContentLoaded",

    async function () {

        await loadCurrentUser();

        await loadResumeList();

        await loadDashboard();

        if (typeof loadReport === "function") {

            await loadReport();

}

    }

);

// ==========================================
// Current User
// ==========================================

async function loadCurrentUser() {

    try {

        const response = await apiRequest(

            "/auth/me",

            {

                method: "GET",

                headers: authHeaders()

            }

        );

        const result = await response.json();

        document.getElementById(

            "userName"

        ).innerHTML =

            result.data.full_name;

        document.getElementById(

            "profileName"

        ).innerHTML =

            result.data.full_name;

        document.getElementById(

            "profileEmail"

        ).innerHTML =

            result.data.email;

    }

    catch (error) {

        console.error(error);

    }

}

// ==========================================
// Load Dashboard
// ==========================================

async function loadDashboard() {

    try {

        const resumeId =

            localStorage.getItem(

                "resume_id"

            );

        if (!resumeId) {

            return;

        }

        const response = await apiRequest(

            "/resume/dashboard/" +

            resumeId,

            {

                method: "GET",

                headers: authHeaders()

            }

        );

        const result =

            await response.json();

        updateDashboard(

            result.data

        );

    }

    catch (error) {

        console.error(error);

    }

}

// ==========================================
// Update Dashboard
// ==========================================

function updateDashboard(data) {

    document.getElementById("atsScore").innerHTML =
        data.summary.ats_score ?? "--";

    document.getElementById("placementProbability").innerHTML =
        data.summary.placement_probability ?? "--";

    document.getElementById("salaryPrediction").innerHTML =
        data.summary.predicted_salary ?? "--";

    document.getElementById("careerRecommendation").innerHTML =
        data.summary.career ?? "--";

    // Charts Load
    loadCharts(data);

}