// ==========================================
// Career AI Report
// ==========================================

async function loadReport() {

    try {

        const resumeId = localStorage.getItem("resume_id");

        if (!resumeId) {

            return;

        }

        const response = await apiRequest(

            "/resume/dashboard/" + resumeId,

            {

                method: "GET",

                headers: authHeaders()

            }

        );

        const result = await response.json();

        if (!response.ok) {

            alert(result.detail || "Unable to load report.");

            return;

        }

        renderReport(result.data);

        loadResumeName();

    }

    catch (error) {

        console.error(error);

    }

}

// ==========================================
// Resume Name
// ==========================================

async function loadResumeName() {

    try {

        const resumeId = localStorage.getItem("resume_id");

        const response = await apiRequest(

            "/resume/",

            {

                method: "GET",

                headers: authHeaders()

            }

        );

        const result = await response.json();

        const resume = result.data.find(

            r => r.id == resumeId

        );

        if (resume) {

            document.getElementById(

                "reportResumeName"

            ).innerHTML = resume.original_filename;

        }

    }

    catch (error) {

        console.error(error);

    }

}

// ==========================================
// Render Report
// ==========================================

function renderReport(data) {

    // Summary

    document.getElementById("reportATS").innerHTML =
        data.summary.ats_score ?? "--";

    document.getElementById("reportPlacement").innerHTML =
        data.summary.placement_probability ?? "--";

    document.getElementById("reportSalary").innerHTML =
        data.summary.predicted_salary ?? "--";

    document.getElementById("reportCareer").innerHTML =
        data.summary.career ?? "--";

    // Status

    const badge = document.getElementById("reportStatus");

    const status = data.status || "Analyzed";

    badge.innerHTML = status;

    if (status.toLowerCase() === "completed" || status.toLowerCase() === "analyzed") {

        badge.style.background = "#16a34a";

    }
    else if (status.toLowerCase() === "pending") {

        badge.style.background = "#f59e0b";
    }
    else {

        badge.style.background = "#f59e0b";

    }

    // Skills

    const skills = document.getElementById("reportSkills");

    skills.innerHTML = "";

    (data.skills || []).forEach(

        skill => {

            skills.innerHTML +=

            `<span class="skill-badge">

                ${skill}

            </span>`;

        }

    );

    // Strengths

    renderList(

        "reportStrengths",

        data.strengths

    );

    // Weaknesses

    renderList(

        "reportWeaknesses",

        data.weaknesses

    );

    // Recommendations

    renderList(

        "reportRecommendations",

        data.recommendations

    );

}

// ==========================================
// Render List
// ==========================================

function renderList(id, list) {

    const ul = document.getElementById(id);

    ul.innerHTML = "";

    if (!list || list.length === 0) {

        ul.innerHTML =

        "<li>No Data Available</li>";

        return;

    }

    list.forEach(

        item => {

            ul.innerHTML +=

            `<li>${item}</li>`;

        }

    );

}